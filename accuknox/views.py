import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as mylogin,logout
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .models import FriendRequest
from django.utils import timezone
from datetime import timedelta

# Create your views here.
@csrf_exempt
def signup(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        name = data.get('email').split("@")[0]
        email = data.get('email')
        password = data.get('password')
        user = User.objects.create_user(name, email, password)
        user.save()
        return JsonResponse({'data': 'User Created'}, status=201)
    else:
        return JsonResponse({'Error': 'Error'}, status=401)

@csrf_exempt
def login(request):
    if request.method=="POST":
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            return JsonResponse({'Error': 'User Not Exist'}, status=401)
       
        user = authenticate(username=user.username, password=password)
        if user is not None:
            mylogin(request, user)
            csrf_token = get_token(request)
            return JsonResponse({'data': 'Login success', 'csrf_token': csrf_token}, status=200)
            

        else:
            return JsonResponse({'data': 'Wrong Credentials'}, status=201)
    else:
        return JsonResponse({'Error': 'Error'}, status=401)



@csrf_exempt
def SentFrindRequest(request):
    if request.user.is_authenticated:
        if(request.method == 'POST'):
            data = json.loads(request.body)
            
            try:
                to_user = User.objects.get(username=data.get('username'))
            except User.DoesNotExist:
                return JsonResponse({'error': 'User does not exist'}, status=404)
            if FriendRequest.objects.filter(from_user=request.user, to_user=to_user).exists():
                return JsonResponse({"data":"Request Already Send"},status=201)
            else:
                one_minute_ago = timezone.now() - timedelta(minutes=1)
                recent_requests = FriendRequest.objects.filter(from_user=request.user, created_at__gte=one_minute_ago)
                if recent_requests.count() >= 3:
                    return JsonResponse({'error': 'Cannot send more than 3 friend requests within a minute'}, status=200)


                FriendRequest.objects.create(from_user=request.user,to_user=to_user,status="pending")
                return JsonResponse({"data":"Request Send"},status=201)
    else:
            return JsonResponse({"Message":"Login First"},status=400)
@csrf_exempt
def RejectFrindRequest(request):
    if request.user.is_authenticated:
        if(request.method == 'POST'):
            data = json.loads(request.body)
            
            try:
                to_user = User.objects.get(username=data.get('username'))
            except User.DoesNotExist:
                return JsonResponse({'error': 'User does not exist'}, status=404)

            if FriendRequest.objects.filter(from_user=request.user, to_user=to_user,status="pending").exists():
                FriendRequest.objects.filter(from_user=request.user, to_user=to_user, status="pending").delete()

                return JsonResponse({"data":"Request Rejected"},status=201)
            else:
                return JsonResponse({"data":"No Request Found"},status=201)
    else:
            return JsonResponse({"Message":"Login First"},status=400)
@csrf_exempt
def AcceptFriendRequest(request):
    if request.user.is_authenticated:
        if(request.method == 'POST'):
            data = json.loads(request.body)
            
            try:
                from_user = User.objects.get(username=data.get('username'))
            except User.DoesNotExist:
                return JsonResponse({'error': 'User does not exist'}, status=404)

            print(FriendRequest.objects.filter(from_user=from_user, to_user=request.user,status="pending"))
            if FriendRequest.objects.filter(from_user=from_user, to_user=request.user,status="pending").exists():
                r = FriendRequest.objects.get(from_user=from_user, to_user=request.user, status="pending")
                r.status = "accepted"
                r.save()

                return JsonResponse({"data":"Request Accepted"},status=201)
            else:
                return JsonResponse({"data":"No Request Found"},status=201)
    else:
            return JsonResponse({"Message":"Login First"},status=400)

@csrf_exempt
def ListOfFriends(request):
    if request.user.is_authenticated:
            data = []
            x = FriendRequest.objects.filter(to_user=request.user,status='accepted')
            for i in x:
                data.append(i.from_user.username)
            
            x = FriendRequest.objects.filter(from_user=request.user,status='accepted')
            for i in x:
                data.append(i.to_user.username)
            return JsonResponse({"data":data},status=201)
    else:
            return JsonResponse({"Message":"Login First"},status=400)       
        

@csrf_exempt
def SearchUsers(request):
    if request.user.is_authenticated:
        if(request.method == 'POST'):
            z = json.loads(request.body)
            keyword = z.get("keyword")
            page_no = int(z.get("page_no"))
            end = page_no*10
            start = end-9
            data = []
            if '@' in keyword:
                x = User.objects.get(email= keyword)
                data.append(x.username)
            else:
                x = User.objects.filter(username__icontains=keyword)
                if(len(x)<=10):
                    for i in x:
                        data.append(i.username)
                else:
                    for i in range(start,end+1):
                        data.append(x[i].username)
            return JsonResponse({"data":data},status=201)
    else:
            return JsonResponse({"Message":"Login First"},status=400)
@csrf_exempt
def PendingRequests(request):
    if request.user.is_authenticated:
            data = []
            x = FriendRequest.objects.filter(to_user=request.user,status='pending')
            for i in x:
                data.append(i.to_user.username)
            return JsonResponse({"data":data},status=201)
    else:
            return JsonResponse({"Message":"Login First"},status=400)



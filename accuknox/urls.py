from django.urls import path
from .views import signup,login,SentFrindRequest,RejectFrindRequest,AcceptFriendRequest,ListOfFriends,SearchUsers,PendingRequests

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),

    path('SendRequest/', SentFrindRequest, name='SentFrindRequest'),
    path('RejectRequest/', RejectFrindRequest, name='RejectFrindRequest'),
    path('AcceptRequest/', AcceptFriendRequest, name='AcceptFriendRequest'),
    path('ListOfFriends/', ListOfFriends, name='ListOfFriends'),
    path('PendingRequests/', PendingRequests, name='PendingRequests'),
    path('SearchUsers/', SearchUsers, name='SearchUsers'),
    
    
    
    
]

from django.contrib.auth.models import User
from django.db import models


class FriendRequest(models.Model):
    from_user =   models.ForeignKey(User,related_name='sent_requests',on_delete=models.CASCADE)
    to_user =   models.ForeignKey(User,related_name='received_requests',on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.created_at)
    class Meta:
        unique_together = ('from_user', 'to_user')
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users (AbstractUser):
    phone = models.CharField(max_length=20, blank=True, name=True)
    avatar = models.ImageField(upload_to='', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
    
class conversation(models.Model):
  user= models.ForeignKey(Users, on_delete=models.CASCADE)
  participants = models.ManyToManyField(Users)
  created_at = models.DateTimeField(auto_now_add=True)

class message (models.Model):
   chat_group = models.ForeignKey(conversation, related_name='messages', on_delete=models.CASCADE)
   sender = models.ForeignKey(Users, on_delete=models.CASCADE)
   text = models.TextField()
   timestamp = models.DateTimeField(auto_now_add=True)


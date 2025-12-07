from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from .managers import UnreadMessagesManager


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    

    edited_at = models.DateTimeField(null=True, blank=True)
    edited_by = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='edited_messages'
    )
    
    parent_message = models.ForeignKey('self',
                                       on_delete=models.CASCADE,
                                       null=True,
                                       blank=True,
                                       related_name='replies'
                                       )
    read = models.BooleanField(default=False)
    objects = models.Manager()
    unread = UnreadMessagesManager()

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"


class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='notifications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user} - Message ID {self.message.id}"

class MessageHistory(models.Model):
    user = models.ForeignKey(User, related_name='message_history', on_delete=models.CASCADE)
    message= models.ForeignKey(Message, on_delete=models.CASCADE, related_name='message_history')
    old_content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
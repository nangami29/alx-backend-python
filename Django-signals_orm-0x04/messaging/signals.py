from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from.models import Message, Notification, MessageHistory
from django.contrib.auth.models import User
@receiver(post_save, sender = Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user = instance.receiver,
            message= instance
        )

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
       if instance.pk:
            old_message = Message.objects.get(pk=instance.pk)
            try:
                 if old_message.content != instance.content:
                    MessageHistory.objects.create(
                    user=instance.sender,
                    message=instance,
                    old_content=old_message.content
                )
                    instance.edited = True
                
            except Message.DoesNotExist:
                pass 
  
       
            
       



@receiver(post_delete, sender=User)
def delete_user(sender, instance,  **kwargs):
    Message.objects.filter(sender=instance).delete()
    Notification.objects.filter(user=instance).delete()
    MessageHistory.objects.filter(user=instance).delete()
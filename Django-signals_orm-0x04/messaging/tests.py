from django.test import TestCase
from .models import Message, Notification
from django.contrib.auth.models import User
# Create your tests here.
class NotificationSignalTest(TestCase):
    def test_notication_created(self):
        user_a=User.objects.create_user(username='Alice')
        user_b=User.objects.create_user(username= 'Bob')
        Message.objects.create(sender=user_a, receiver=user_b, content="Hello!")

        self.assertEqual(Notification.objects.count(), 1)
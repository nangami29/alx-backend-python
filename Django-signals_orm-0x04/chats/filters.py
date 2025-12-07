import django_filters
from .models import message
class MessageFilter(django_filters.FilterSet):
    class Meta:
        model = message
        fields = {'chat_group': ['exact'],
                   'sender': ['exact'], 'text':['icontains'],
                     'timestamp': ['gte', 'lte']}
                
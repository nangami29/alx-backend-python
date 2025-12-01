from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import conversation, message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MessageFilter
from .pagination import MessagePagination

# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
    queryset= conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes =[IsParticipantOfConversation] 
class MessageViewSet(viewsets.ModelViewSet):
    queryset = message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter
    pagination_class = MessagePagination
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from django.views.decorators.cache import cache_page
# Create your views here.
@login_required
def delete_user(request):
    if request.method == 'POST':
        user=request.user.delete()
        
        return redirect('home')
    return render(request, 'confirm_delete.html')



def message_thread(request):

    messages = Message.objects.filter(
        parent_message__isnull=True
    ).filter(
        sender=request.user
    ).select_related(
        'sender', 'receiver'
    ).prefetch_related(
        'replies'
    )

    return render(request, 'messaging/thread.html', {'messages': messages})
@cache_page(60)
def conversation_view(request):
    messages = Message.objects.select_related('sender', 'receiver').prefetch_related('replies').all()
    
    context = {'messages': messages}
    return render(request, 'chats/conversation.html', context)

def unread_messages_view(request):
    unread_messages = Message.unread.unread_for_user(request.user).only('id', 'sender', 'content', 'timestamp')

    context = {
        'messages': unread_messages
    }
    return render(request, 'messaging/unread_inbox.html', context)
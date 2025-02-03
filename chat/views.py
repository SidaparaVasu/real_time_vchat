from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Message
from django.db.models import Q

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def user_login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse('login_request'))
    return _wrapped_view

@user_login_required
def render_home(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user
    return render(request, 'home.html', {'users': users})

@user_login_required
def chat_room(request, room_name):

    other_users = User.objects.exclude(id=request.user.id) 
    
    chats = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver__username=room_name)) |
        (Q(receiver=request.user) & Q(sender__username=room_name))
    )

    chats = chats.order_by('timestamp') 
    user_last_messages = []

    for user in other_users:
        last_message = Message.objects.filter(
            (Q(sender=request.user) & Q(receiver=user)) |
            (Q(receiver=request.user) & Q(sender=user))
        ).order_by('-timestamp').first()

        user_last_messages.append({
            'user': user,
            'last_message': last_message
        })

    return render(request, 'home.html', {
        'room_name': room_name,
        'chats': chats,
        'other_users': other_users,
        'user_last_messages': user_last_messages,
    })
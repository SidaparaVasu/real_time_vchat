from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from chat.views import chat_room

# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "Registration successful." )

            return redirect(f'/chat/{user.username}/')
        
        messages.error(request, "Unsuccessful registration. Invalid information.")
    
    form = NewUserForm()
    return render(request, 'register.html')


def login_page(request):
    return render(request, 'login.html')

def login_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")
            
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            # messages.info(request, f"You are now logged in as {username}.")

            return redirect(f'/chat/{username}/')
        else:
            messages.error(request,"Invalid email or password.")
    else:
        messages.error(request,"Invalid email or password.")
    
    form = AuthenticationForm()
    return render(request, 'login.html')


def logout_request(request):
    logout(request)
    return render(request, 'login.html')
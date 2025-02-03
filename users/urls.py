from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name="login_page"),
    path('login_request', views.login_request, name="login_request"),
    path('register', views.register_user, name='register_user'),
    path('logout', views.logout_request, name= "logout_request"),
] 
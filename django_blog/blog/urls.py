from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns = [
  path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
  path('logout/', LogoutView.as_view(next_page='blog/login.html'), name='logout'),
  path('register/', register, name='register')
]
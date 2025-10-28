from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profileView
from . import views

urlpatterns = [
  path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
  path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
  path('register/', register, name='register'),
  path('profile/', profileView, name='profile'),
  path('posts/', views.BlogListView.as_view(), name='blog_list'),
  path('posts/create', views.BlogCreateView.as_view(), name='blog_create'),
  path('posts/post<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
  path('posts/post<int:pk>/update', views.BlogUpdateView.as_view(), name='blog_update'),
  path('posts/post<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog_delete'),
  path('posts/post<int:pk>/comment_list', views.CommentListView.as_view(), name='comment_list'),
  path('posts/post<int:pk>/comment_create', views.CommentCreateView.as_view(), name='comment_create'),
  path('posts/post<int:pk>/comment_update', views.CommentCreateView.as_view(), name='comment_update'),
  path('posts/post<int:pk>/comment_delete', views.CommentDeleteView.as_view(), name='comment_delete'),
]
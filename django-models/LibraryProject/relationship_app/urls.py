from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('list/', views.list_books, name='books_list'),
  path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_details'),
  path('register/', views.register, name='register'),
  path('', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
  path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
]
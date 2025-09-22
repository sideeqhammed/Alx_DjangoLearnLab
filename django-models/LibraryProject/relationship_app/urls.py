from django.urls import path
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('books/', list_books, name='books_list'),
  path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_details'),
  path('register/', register, name='register'),
  path('', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
  path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
]
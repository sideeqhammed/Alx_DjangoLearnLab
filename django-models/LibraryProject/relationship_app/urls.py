from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('books/', views.list_books, name='books_list'),
  path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_details'),
  path('register/', views.register, name='register'),
  path('', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
  path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
  path('admin/', views.admin_page, name='admin'),
  path('librarian/', views.librarian_page, name='librarian'),
  path('member/', views.member_page, name='member'),
  path('books/add_book/', views.add_book_view, name='add_book'),
  path('books/<int:pk>/edit_book/', views.edit_book_view, name='edit_book'),
  path('books/<int:pk>/delete_book/', views.delete_book_view, name='add_book'),
]
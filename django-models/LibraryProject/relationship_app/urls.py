from django.urls import path
from . import views, admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('list/', views.list_books, name='books_list'),
  path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_details'),
  path('register/', views.register, name='register'),
  path('', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
  path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
  path('admin/', admin_view.admin_page, name='admin'),
  path('librarian/', librarian_view.librarian_page, name='librarian'),
  path('member/', member_view.member_page, name='member'),
]
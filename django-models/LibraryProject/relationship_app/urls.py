from django.urls import path
from .views import List_books, LibraryDetailView

urlpatterns = [
  path('books/', List_books, name='book_list'),
  path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_details'),
]
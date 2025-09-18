from django.urls import path
from .views import List_books, LibraryDetails

urlpatterns = [
  path('books/', List_books, name='book_list'),
  path('libraries/<int:pk>/', LibraryDetails.as_view(), name='library_details'),
]
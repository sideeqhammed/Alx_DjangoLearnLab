from django.urls import path
from .views import books_view, LibraryDetails

urlpatterns = [
  path('books/', books_view, name='book_list'),
  path('libraries/<int:pk>/', LibraryDetails.as_view(), name='library_details'),
]
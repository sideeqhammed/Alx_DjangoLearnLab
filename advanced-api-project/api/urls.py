from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from .views import BookListApiView, BookDetailApiView, BookCreateApiView, BookUpdateApiView, BookDeleteApiView

urlpatterns = [
  path('', BookListApiView.as_view(), name='book-api-list'),
  path('<int:pk>/', BookDetailApiView.as_view(), name='book-api-detail'),
  path('createapi/', BookCreateApiView.as_view(), name='create-api-book'),
  path('updateapi/', BookUpdateApiView.as_view(), name='update-api-book'),
  path('deleteapi/', BookDeleteApiView.as_view(), name='delete-api-book'),



  path('books/', BookListView.as_view(), name='book-list'),
  path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
  path('books/create/', BookCreateView.as_view(), name='create-book'),
  path('books/update/', BookUpdateView.as_view(), name='update-book'),
  path('books/delete/', BookDeleteView.as_view(), name='delete-book'),
]
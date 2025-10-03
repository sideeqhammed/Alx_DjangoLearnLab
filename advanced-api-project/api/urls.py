from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
  path('', BookListView.as_view(), name='book-list'),
  path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
  path('add', BookCreateView.as_view(), name='add-book'),
  path('update', BookUpdateView.as_view(), name='update-book'),
  path('delete/', BookDeleteView.as_view(), name='delete-book')
]
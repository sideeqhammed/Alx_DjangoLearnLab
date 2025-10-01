from django.urls import path
from .views import BookList

urlpatterns = [
  path('Books/', BookList.as_view(), name='book-list')
]
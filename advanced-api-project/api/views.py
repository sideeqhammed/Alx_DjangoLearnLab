from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import BookSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class BookListApiView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['title', 'author__name', 'publication_year']
  search_fields = ['title', 'author__name']
  ordering_fields = ['title', 'publication_year']

class BookDetailApiView(generics.RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateApiView(generics.CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

class BookUpdateApiView(generics.UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

class BookDeleteApiView(generics.DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]













class BookListView(ListView):
  model = Book
  template_name = 'api/book_list.html'
  context_object_name = 'books'

class BookDetailView(DetailView):
  model = Book
  template_name = 'api/book_detail.html'
  context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, CreateView):
  model = Book
  template_name = 'api/book_form.html'
  fields = ['title','author', 'publication_year']
  success_url = reverse_lazy('book-list')

class BookUpdateView(LoginRequiredMixin, UpdateView):
  model = Book
  template_name = 'api/book_form.html'
  fields = ['title', 'author', 'publication_year']
  success_url = reverse_lazy('book-list')

class BookDeleteView(LoginRequiredMixin, DeleteView):
  model = Book
  template_name = 'api/book_delete.html'
  success_url = reverse_lazy('book-list')
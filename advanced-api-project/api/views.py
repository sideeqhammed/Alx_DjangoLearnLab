from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
# from .serializers import BookSerializer

# Create your views here.
class BookListView(ListView):
  model = Book
  template_name = 'api/book_list.html'
  context_object_name = 'books'
  permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(DetailView):
  model = Book
  template_name = 'api/book_detail.html'
  context_object_name = 'book'
  permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(LoginRequiredMixin, CreateView):
  model = Book
  template_name = 'api/book_form.html'
  fields = ['title','author', 'publication_year']
  success_url = reverse_lazy('book-list')
  permission_classes = [IsAuthenticated]

class BookUpdateView(LoginRequiredMixin, UpdateView):
  model = Book
  template_name = 'api/book_form.html'
  fields = ['title', 'author', 'publication_year']
  success_url = reverse_lazy('book-list')
  permission_classes = [IsAuthenticated]

class BookDeleteView(LoginRequiredMixin, DeleteView):
  model = Book
  template_name = 'api/book_delete.html'
  success_url = reverse_lazy('book-list')
  permission_classes = [IsAuthenticated]
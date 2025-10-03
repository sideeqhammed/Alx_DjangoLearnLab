from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
# from .serializers import BookSerializer

# Create your views here.
class BookListView(ListView):
  model = Book
  template_name = 'api/book_list.html'
  context_object_name = 'books'

class BookDetailView(DetailView):
  model = Book
  template_name = 'api/book_detail.html'
  context_object_name = 'book'

class BookCreateView(CreateView):
  model = Book
  template_name = 'api/book_form.html'
  fields = ['title','author', 'publication_year']
  success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
  model = Book
  template_name = 'api/book_form.html'
  fields = ['title', 'author', 'publication_year']
  success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
  model = Book
  template_name = 'api/book_delete.html'
  success_url = reverse_lazy('book-list')
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book

# Create your views here.
def books_view(request):
  books = Book.objects.all()
  return render (request, "relationship_app/list_books.html", {books: books})

class LibraryDetails (DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'
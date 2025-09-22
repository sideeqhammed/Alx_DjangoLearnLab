from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from .models import Library, Book
from .form import register_form

# Create your views here.
def list_books (request):
  books = Book.objects.all()
  return render (request, "relationship_app/list_books.html", {'books': books})

class LibraryDetailView (DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'

def register (request):
  if request.method == "POST":
    form = register_form(request.POST)
    if form.is_valid:
      user = form.save()
      login(request, user)
      redirect('login')
  else:
    form = register_form()
    
  context = {'form':form}

  return render(request, 'relationship_app/register.html', context)

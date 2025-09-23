from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Library, Book
from .role_checks import is_admin, is_librarian, is_member
from django.contrib.auth.decorators import user_passes_test

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
    form = UserCreationForm(request.POST)
    if form.is_valid:
      user = form.save()
      login(request, user)
      redirect('books_list')
  else:
    form = UserCreationForm()

  context = {'form':form}

  return render(request, 'relationship_app/register.html', context)

@user_passes_test(is_admin, login_url='login')
def admin_page (request):
  return render(request, 'relationship_app/admin_view.html', {'message':'Welcome, Admin'})

@user_passes_test(is_librarian, login_url='login')
def librarian_page (request):
  return render(request, 'relationship_app/librarian_view.html', {'message':'Welcome, Librarian'})

@user_passes_test(is_member, login_url='login')
def member_page (request):
  return render(request, 'relationship_app/member_view.html', {'message':'Welcome, Member'})
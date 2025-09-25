from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Library, Book
from .role_checks import is_admin, is_librarian, is_member
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

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
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('books_list')
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


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view (request):
  if request.method == 'POST':
    title = request.POST.get('title')
    author = request.POST.get('author')
    Book.objects.create(title=title, author=author)
    return redirect('books_list')
  return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view (request, book_id):
  book = get_object_or_404(Book, id=book_id)
  if request.method == 'POST':
    book.title = request.POST.get('title')
    book.author = request.POST.get('author')
    book.save()
    return redirect('books_list', 'relationship_app/edit_book.html', {'book':book})
  
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book_view(request, book_id):
  book = get_object_or_404(Book, id=book_id)
  if request.method == "POST":
    book.delete()
    return redirect("book_list")
  return render(request, "relationship_app/confirm_delete.html", {"book": book})


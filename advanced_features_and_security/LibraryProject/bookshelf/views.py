from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from .forms import ExampleForm
from django.contrib.auth.decorators  import permission_required

# Create your views here.

def book_list_view(request):
  books = Book.objects.all()
  context = {'books':books}
  return render(request, 'bookshelf/book_list.html', context)

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def add_book_view(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('book_list')
  else:
    form = BookForm()
  return render(request, 'bookshelf/add_book.html', {'form':form})

from django.shortcuts import render

# Create your views here.
def books_view(request):
  return render (request, "list_books.html")
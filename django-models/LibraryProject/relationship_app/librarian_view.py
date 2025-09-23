from .role_checks import is_librarian
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(is_librarian, login_url='login')
def librarian_page (request):
  return render(request, 'relationship_app/librarian_page.html', {'message':'Welcome, Librarian'})
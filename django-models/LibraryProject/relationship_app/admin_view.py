from .role_checks import is_admin
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(is_admin, login_url='login')
def admin_page (request):
  return render(request, 'relationship_app/admin_page.html', {'message':'Welcome, Admin'})
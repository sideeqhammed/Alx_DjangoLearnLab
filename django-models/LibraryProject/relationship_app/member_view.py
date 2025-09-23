from .role_checks import is_member
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(is_member, login_url='login')
def admin_page (request):
  return render(request, 'relationship_app/member_page.html', {'message':'Welcome, Member'})
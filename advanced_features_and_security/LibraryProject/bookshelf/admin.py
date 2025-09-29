from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  list_display = ["title", "author", "publication_year"]
  list_filter = ["author", "publication_year"]
  search_fields = ["title", "author"]
  pass

admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
  list_display = ('username', "email", "date_of_birth", "is_staff", "is_superuser")
  list_filter = ("is_staff", "is_superuser", "is_active")
  search_fields = ("username", "email")


admin.site.register(CustomUser, CustomUserAdmin)
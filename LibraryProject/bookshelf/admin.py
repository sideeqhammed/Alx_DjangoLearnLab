from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  list_display = ["title", "author", "publication_year"]
  list_filter = ["author", "publication_year"]
  pass

admin.site.register(Book)
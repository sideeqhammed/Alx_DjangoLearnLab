from django.test import TestCase
from .models import Book, Author

# Create your tests here.
class AuthorTestCase(TestCase):
  def setUp(self):
    Author.objects.create(name='Harper Lee')
    Author.objects.create(name='F. Scott Fitzgerald')

  def test_author(self):
    author1 = Author.objects.get(name='Harper Lee')
    author2 = Author.objects.get(name='F. Scott Fitzgerald')
    self.assertEqual(str(author1), 'Harper Lee')
    self.assertEqual(str(author2), 'F. Scott Fitzgerald')


class BookTestCase(TestCase):
  def setUp(self):
    author1 = Author.objects.create(name='Harper Lee')
    author2 = Author.objects.create(name='F. Scott Fitzgerald')
    Book.objects.create(title='To Kill a Mockingbird', author=author1, publication_year=1960)
    Book.objects.create(title='The Great Gatsby',	author=author2,	publication_year=1925)

  def test_book(self):
    # checks for books
    book1 = Book.objects.get(title='To Kill a Mockingbird')
    book2 = Book.objects.get(title='The Great Gatsby')
    self.assertEqual(str(book1), 'To Kill a Mockingbird by Harper Lee - 1960')
    self.assertEqual(str(book2), 'The Great Gatsby by F. Scott Fitzgerald - 1925')
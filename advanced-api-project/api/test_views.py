from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from .models import Book, Author
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token

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
    self.book1 = Book.objects.create(title='To Kill a Mockingbird', author=author1, publication_year=1960)
    self.book2 = Book.objects.create(title='The Great Gatsby',	author=author2,	publication_year=1925)

  def test_book(self):
    # checks for books
    self.assertEqual(str(self.book1), 'To Kill a Mockingbird by Harper Lee - 1960')
    self.assertEqual(str(self.book2), 'The Great Gatsby by F. Scott Fitzgerald - 1925')


class BookTestCase(APITestCase):
  def setUp(self):

    # create users
    self.user = User.objects.create(username='john', password='john123')
    self.client = APIClient()
    author1 = Author.objects.create(name='Harper Lee')
    author2 = Author.objects.create(name='F. Scott Fitzgerald')
    self.book1 = Book.objects.create(title='To Kill a Mockingbird', author=author1, publication_year=1960)
    self.book2 = Book.objects.create(title='The Great Gatsby',	author=author2,	publication_year=1925)

  def test_book_list(self):
    response = self.client.get('/library/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)

  def test_book_details(self):
    url = reverse(viewname='book-api-detail', args=[self.book1.id])
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], 'To Kill a Mockingbird')

  def test_book_create_unauthorized(self):
    url = reverse('create-api-book')
    author = Author.objects.create(name='Charles Dickens')
    data = {
      'title' : 'A Tale of Two Cities',
      'author' : author,
      'publication_year' : 1859,
    }
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


  def test_book_create_authorized(self):
    token = Token.objects.create(user=self.user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    url = reverse('create-api-book')
    author = Author.objects.create(name='Charles Dickens')
    data = {
      'title' : 'A Tale of Two Cities',
      'author' : author.id,
      'publication_year' : 1859,
    }
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 3)

   
from django.test import TestCase
from rest_framework.test import APITestCase
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
    self.user = User.objects.create_user(username='john', password='john123')

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
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_book_create_authorized(self):
    self.client.login(username='john', password='john123')

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

  def test_book_update_unauth(self):
    url = reverse('update-api-book', args=[self.book2.id])
    data = {'title': 'The Great Gatsby Copy'}
    response = self.client.patch(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    self.book2.refresh_from_db()
    self.assertEqual(self.book2.title, 'The Great Gatsby')

  def test_book_update_auth(self):
    self.client.login(username='john', password='john123')

    url = reverse('update-api-book', args=[self.book2.id])
    data = {'title': 'The Great Gatsby Copy'}
    response = self.client.patch(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book2.refresh_from_db()
    self.assertEqual(self.book2.title, 'The Great Gatsby Copy')
   
  def test_book_delete_unauth(self):
    url = reverse('delete-api-book', args=[self.book2.id])
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    self.assertEqual(Book.objects.count(), 2)

  def test_book_delete_auth(self):
    self.client.login(username='john', password='john123')

    url = reverse('delete-api-book', args=[self.book2.id])
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 1)
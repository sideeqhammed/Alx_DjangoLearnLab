from rest_framework import serializers
from .models import Book, Author
import datetime

# book serializer class
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['title', 'publication_year', 'author']

    # validates if the year provided is not in the future
    def validate(self, data):
      if data['publication_year'] > datetime.now().year:
        raise serializers.ValidationError(f'Year cannot be higher than {datetime.now().year}')
      return data

# author serializer class that includes a nested bookserializer, this allows the api to return the author along with his books
class AuthorSerializer(serializers.ModelSerializer):
  books = BookSerializer(many=True, read_only=True)
  
  class Meta:
    model = Author
    fields = ['name', 'books']

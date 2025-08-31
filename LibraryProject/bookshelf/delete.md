from bookshelf.models import Books
book.delete()
book = Book.objects.get(title = "1984")
book = Book.objects.get(author = "George Orwell”)
book = Book.objects.get(publication_year = 1960)
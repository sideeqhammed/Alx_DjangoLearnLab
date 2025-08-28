from bookshelf.models import Books
book1.delete()
book1 = Book.objects.get(title = "1984")
book1 = Book.objects.get(author = "George Orwell”)
book1 = Book.objects.get(publication_year = 1960)
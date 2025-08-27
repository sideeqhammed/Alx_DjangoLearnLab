from bookshelf.models import Books
book1 = Book.objects.create(title="1984", author="George Orwell”, publication_year=1949)
book1.save()
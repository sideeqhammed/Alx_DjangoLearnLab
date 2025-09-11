# Checks for List of all books in a library.
library = Library.objects.get(name=library_name)
books = library.books.all()

# Checks for all books by a specific author
books = Book.objects.filter(author=author_name)

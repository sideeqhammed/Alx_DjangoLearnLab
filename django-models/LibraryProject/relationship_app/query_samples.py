# Checks for List of all books in a library.
library = Library.objects.get(name=library_name)
books = library.books.all()

# Checks for all books by a specific author
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

# Retrieve the librarian of a library
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
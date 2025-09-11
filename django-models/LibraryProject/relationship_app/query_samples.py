library = Library.objects.get(name=library_name)
books = library.books.all()
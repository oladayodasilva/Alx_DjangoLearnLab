# Create Books in Django Shell

```python
from bookshelf.models import Book

b1 = Book.objects.create(title='1984', author='George Orwell', 
publication_year=1949)
b2 = Book.objects.create(title='The Great Gatsby', author='F. Scott 
Fitzgerald', publication_year=1925)
Book.objects.all()


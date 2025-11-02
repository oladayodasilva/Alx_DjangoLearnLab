### Django Admin Setup for Book Model

1. Registered the `Book` model in `bookshelf/admin.py`.
2. Customized the admin interface using the `BookAdmin` class.
   - Displayed `title`, `author`, and `publication_year` in the list view.
   - Enabled search by `title` and `author`.
   - Added a filter by `publication_year`.
3. Created a superuser using:
   ```bash
   python3 manage.py createsuperuser


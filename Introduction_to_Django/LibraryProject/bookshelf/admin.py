from django.contrib import admin
from .models import Book

# Customize how Book entries appear in the admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# Register the model with the admin site
admin.site.register(Book, BookAdmin)


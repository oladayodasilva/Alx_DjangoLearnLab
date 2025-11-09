# relationship_app/urls.py

from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register_view,
    login_view,
    logout_view,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book
)

urlpatterns = [
    # Task 1: Library Views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), 
name='library_detail'),

    # Task 2: Authentication Views
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Task 3: Role-Based Views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Task 4: Permission-Protected Book Views
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]



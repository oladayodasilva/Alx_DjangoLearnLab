from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'description', 'publication_date', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')


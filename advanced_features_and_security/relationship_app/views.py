# relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Import your models and forms
from .models import Book  # Replace/add other models
from .forms import BookForm, CustomUserCreationForm  # Replace/add other forms

# ------------------------------
# Authentication Views
# ------------------------------

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect after logout

# ------------------------------
# User Registration View
# ------------------------------

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# ------------------------------
# Dashboard View
# ------------------------------

@login_required
def dashboard(request):
    return render(request, 'relationship_app/dashboard.html')

# ------------------------------
# Book Management Views
# ------------------------------

@login_required
@permission_required('relationship_app.can_add_book', 
raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('dashboard')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# ------------------------------
# Class-Based Example Views
# ------------------------------

@method_decorator(login_required, name='dispatch')
class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'relationship_app/book_list.html', {'books': books})

# Optional: Permission-protected class-based view
@method_decorator(permission_required('relationship_app.can_add_book', raise_exception=True), name='dispatch')
class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'relationship_app/add_book.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book_list')
        return render(request, 'relationship_app/add_book.html', {'form': form})


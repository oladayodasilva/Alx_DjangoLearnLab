from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, 
permission_required

from .models import Book, Library, UserProfile

# ----------------------------
# Task 0 & 1: Book & Library Views
# ----------------------------

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': 
books})

# Class-based view: detail of a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ----------------------------
# Task 2: Authentication Views
# ----------------------------

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': 
form})

# ----------------------------
# Task 3: Role-Based Access Views
# ----------------------------

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# ----------------------------
# Task 4: Permission-Secured Views
# ----------------------------

@permission_required('relationship_app.add_book', raise_exception=True)
def add_book(request):
    # implement your add book logic here
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.change_book', raise_exception=True)
def edit_book(request, book_id):
    # implement your edit book logic here
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.delete_book', raise_exception=True)
def delete_book(request, book_id):
    # implement your delete book logic here
    return render(request, 'relationship_app/delete_book.html')


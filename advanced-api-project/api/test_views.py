from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User

from api.models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username="user1", password="password123")
        self.admin = User.objects.create_superuser(username="admin", password="admin123")

        # Create author
        self.author = Author.objects.create(name="Test Author")

        # Create books
        self.book1 = Book.objects.create(
            title="Alpha Book",
            author=self.author,
            publication_year=2001
        )
        self.book2 = Book.objects.create(
            title="Beta Book",
            author=self.author,
            publication_year=2005
        )

        # API Client
        self.client = APIClient()

        # URL paths
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.id})
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.id})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.id})

    # -----------------------------------------------------------
    # LIST / FILTER / SEARCH / ORDERING TESTS
    # -----------------------------------------------------------

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {"title": "Alpha Book"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Alpha Book")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Beta"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering_books(self):
        response = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Alpha Book")

    # -----------------------------------------------------------
    # CREATE TESTS
    # -----------------------------------------------------------

    def test_create_book_requires_authentication(self):
        response = self.client.post(self.create_url, {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2020
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username="user1", password="password123")
        response = self.client.post(self.create_url, {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2020
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # -----------------------------------------------------------
    # UPDATE TESTS
    # -----------------------------------------------------------

    def test_update_book_requires_authentication(self):
        response = self.client.put(self.update_url, {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2021
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        self.client.login(username="user1", password="password123")
        response = self.client.put(self.update_url, {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2021
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    # -----------------------------------------------------------
    # DELETE TESTS
    # -----------------------------------------------------------

    def test_delete_book_requires_authentication(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        self.client.login(username="user1", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())


from django.test import TestCase
from .models import Book

class BookCRUDTests(TestCase):
    def test_create_book(self):
        book = Book.objects.create(title="Test Book", author="Test Author")
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(book.title, "Test Book")

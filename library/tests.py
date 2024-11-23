from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def test_string_representation(self):
        book = Book(title="A Sample Book")
        self.assertEqual(str(book), book.title)
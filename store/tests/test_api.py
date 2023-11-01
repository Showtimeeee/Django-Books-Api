from django.urls import reverse
from rest_framework.test import APITestCase

from store.models import Book


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.object.create(name='Test book 1', price=25)
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        print(response)
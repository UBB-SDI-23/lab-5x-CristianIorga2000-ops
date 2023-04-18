from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Author, Book, Authorship, Review

class AuthorViewSetTestCase(APITestCase):
    def setUp(self):
        # create test data
        self.author1 = Author.objects.create(name='Author 1', email='author1@example.com', bio='Bio 1')
        self.author2 = Author.objects.create(name='Author 2', email='author2@example.com', bio='Bio 2')
        self.book1 = Book.objects.create(title='Book 1', summary='Summary 1', published_date='2022-01-01')
        self.book2 = Book.objects.create(title='Book 2', summary='Summary 2', published_date='2022-02-01')
        self.authorship1 = Authorship.objects.create(author=self.author1, book=self.book1, contribution='Contribution 1', royalty_percentage=25)
        self.authorship2 = Authorship.objects.create(author=self.author1, book=self.book2, contribution='Contribution 2', royalty_percentage=10)
        self.authorship3 = Authorship.objects.create(author=self.author2, book=self.book1, contribution='Contribution 3', royalty_percentage=15)

    def test_total_royalty(self):
        url = reverse('author-total-royalty')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        author1_data = next((item for item in response.data if item["id"] == self.author1.id), None)
        self.assertIsNotNone(author1_data)
        self.assertEqual(author1_data['total_royalty'], 35)

        author2_data = next((item for item in response.data if item["id"] == self.author2.id), None)
        self.assertIsNotNone(author2_data)
        self.assertEqual(author2_data['total_royalty'], 15)


class ReviewViewSetTestCase(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(title='Test Book', summary='Test summary', published_date='2022-01-01')
        self.review = Review.objects.create(book=self.book, reviewer_name='John Doe', review_text='Test review', rating=4)

    def test_filter_by_rating_gt(self):
        url = reverse('review-filter-by-rating-gt')
        response = self.client.get(url, {'rating': '3'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.review.id)
        self.assertEqual(response.data[0]['rating'], self.review.rating)
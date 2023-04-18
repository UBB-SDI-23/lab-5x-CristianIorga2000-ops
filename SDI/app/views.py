from rest_framework import viewsets
from .models import Authorship, Author, Book, Review
from .serializers import AuthorSerializer, AuthorshipSerializer, BookSerializer, ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Sum
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination
    
    @action(detail=False)
    def total_royalty(self, request):
        authors = Author.objects.annotate(total_royalty=Sum('authorship__royalty_percentage')).order_by('-total_royalty')
        serializer = self.get_serializer(authors, many=True)
        for i in range(len(serializer.data)):
            serializer.data[i]['total_royalty'] = 0 if authors[i].total_royalty==None else authors[i].total_royalty
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def books(self, request, pk=None):
        author = self.get_object()
        books = request.data
        for book_data in books:
            book_data['author'] = author.id
            serializer = BookSerializer(data=book_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(status=201)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Retrieve all reviews for the book instance
        reviews_queryset = Review.objects.filter(book=instance)
        reviews_serializer = ReviewSerializer(reviews_queryset, many=True)

        # Add the reviews to the serialized response
        serialized_data = serializer.data
        serialized_data['reviews'] = reviews_serializer.data

        return Response(serialized_data)
    
    @action(detail=False)
    def average_rating(self, request):
        books = Book.objects.annotate(avg_rating=Avg('review__rating')).order_by('-avg_rating')
        serializer = self.get_serializer(books, many=True)
        for i in range(len(serializer.data)):
            serializer.data[i]['avg_rating'] = 0 if books[i].avg_rating==None else  books[i].avg_rating

        return Response(serializer.data)
    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = StandardResultsSetPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Retrieve the Book instance associated with the Review instance
        book_instance = instance.book
        book_serializer = BookSerializer(book_instance)

        # Add the Book instance to the serialized response
        serialized_data = serializer.data
        serialized_data['book'] = book_serializer.data

        return Response(serialized_data)
    
    @action(detail=False, methods=['get'])
    def filter_by_rating_gt(self, request):
        rating_gt = request.GET.get('rating')
        if rating_gt:
            reviews = self.queryset.filter(rating__gt=rating_gt)
        else:
            reviews = self.queryset.all()
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)



class AuthorshipViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Authorship.objects.all()
    serializer_class = AuthorshipSerializer
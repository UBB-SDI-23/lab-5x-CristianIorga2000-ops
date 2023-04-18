from rest_framework import serializers
from .models import Authorship, Author, Book, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'


class AuthorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authorship
        fields = '__all__'
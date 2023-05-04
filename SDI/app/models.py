from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
import datetime

# Create your models here.
from django.db import models

# Review 1-n Book
# Book m-n Author (Authorship)

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    published_date = models.DateField(validators=[MaxValueValidator(datetime.date.today)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book} - {self.reviewer_name}"
    

class Authorship(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=100, validators=[MaxLengthValidator(50)])
    royalty_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    role = models.CharField(max_length=50, null=True, blank=True)  # New field

    def __str__(self):
        return f"{self.author.name} - {self.book.title}"

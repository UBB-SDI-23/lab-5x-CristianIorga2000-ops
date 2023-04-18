from django.core.management.base import BaseCommand
from app.models import Author, Authorship, Book, Review
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populate Authors in the database'

    def handle(self, *args, **options):
        authors = [
            Author(
                name='Jane Smith',
                email='jane.smith@gmail.com',
                bio='I am a freelance writer and editor with over 10 years of experience.',
                created_at=datetime.datetime(2022, 3, 19, 12, 30),
                updated_at=datetime.datetime(2022, 3, 20, 10, 15)
            ),
            Author(
                name='John Doe',
                email='john.doe@gmail.com',
                bio='I am a software engineer with a passion for writing.',
                created_at=datetime.datetime(2022, 3, 18, 9, 45),
                updated_at=datetime.datetime(2022, 3, 19, 14, 20)
            ),
            Author(
                name='Anna Lee',
                email='anna.lee@yahoo.com',
                bio='I am a journalist with a focus on environmental issues.',
                created_at=datetime.datetime(2022, 3, 17, 15, 0),
                updated_at=datetime.datetime(2022, 3, 18, 11, 30)
            ),
            Author(
                name='David Kim',
                email='david.kim@hotmail.com',
                bio='I am a novelist and screenwriter.',
                created_at=datetime.datetime(2022, 3, 16, 18, 20),
                updated_at=datetime.datetime(2022, 3, 17, 14, 45)
            ),
            Author(
                name='Maria Rodriguez',
                email='maria.rodriguez@gmail.com',
                bio='I am a poet and translator.',
                created_at=datetime.datetime(2022, 3, 15, 11, 0),
                updated_at=datetime.datetime(2022, 3, 16, 9, 30)
            ),
            Author(
                name='Alex Wong',
                email='alex.wong@yahoo.com',
                bio='I am a technical writer with experience in software development.',
                created_at=datetime.datetime(2022, 3, 14, 14, 30),
                updated_at=datetime.datetime(2022, 3, 15, 12, 15)
            ),
            Author(
                name='Elena Martinez',
                email='elena.martinez@gmail.com',
                bio='I am a historian and writer.',
                created_at=datetime.datetime(2022, 3, 13, 10, 0),
                updated_at=datetime.datetime(2022, 3, 14, 8, 45)
            ),
            Author(
                name='Mark Johnson',
                email='mark.johnson@hotmail.com',
                bio='I am a journalist with a background in investigative reporting.',
                created_at=datetime.datetime(2022, 3, 12, 17, 45),
                updated_at=datetime.datetime(2022, 3, 13, 16, 0)
            ),
            Author(
                name='Ligma Bonz',
                email='li_gmabonz@outlook.fr',
                bio='I am a comediant with very little success and a depressing life due to my rare disease called Ligma.',
                created_at=datetime.datetime(2022, 3, 12, 17, 45),
                updated_at=datetime.datetime(2022, 3, 13, 16, 0)
            )
        ]
        Author.objects.bulk_create(authors)
        self.stdout.write(self.style.SUCCESS(
            'Successfully populated authors.'))

        books = [
            Book(
                title='The Great Gatsby',
                summary='A classic novel about the decadent lifestyle of wealthy Americans in the 1920s.',
                published_date=timezone.datetime(1925, 4, 10),
                created_at=timezone.now(),
                updated_at=timezone.now()
            ),
            Book(
                title='To Kill a Mockingbird',
                summary='A novel about racial injustice and the loss of innocence in a small Southern town.',
                published_date=timezone.datetime(1960, 7, 11),
                created_at=timezone.now(),
                updated_at=timezone.now()
            ),
            Book(
                title='1984',
                summary='A dystopian novel about a totalitarian society where individualism is suppressed.',
                published_date=timezone.datetime(1949, 6, 8),
                created_at=timezone.now(),
                updated_at=timezone.now()
            ),
            Book(
                title='Animal Farm',
                summary='A political allegory about a group of farm animals who rebel against their human farmer.',
                published_date=timezone.datetime(1945, 8, 17),
                created_at=timezone.now(),
                updated_at=timezone.now()
            ),
            Book(
                title='Pride and Prejudice',
                summary='A novel about the social norms and expectations of Georgian England.',
                published_date=timezone.datetime(1813, 1, 28),
                created_at=timezone.now(),
                updated_at=timezone.now()
            ),
            Book(
                title='The Catcher in the Rye',
                summary='A coming-of-age novel about a teenage boy who is disillusioned with society.',
                published_date=timezone.datetime(1951, 7, 16),
                created_at=timezone.now(),
                updated_at=timezone.now()
            ),
            Book(
                title='The Lord of the Rings',
                summary='An epic fantasy novel about a hobbit who sets out to destroy an evil ring.',
                published_date=timezone.datetime(1813, 1, 28),
                created_at=timezone.now(),
                updated_at=timezone.now()
            ),
            Book(
                title='Harry Potter and the Philosopher\'s Stone',
                summary='A fantasy novel about a hairy potter that philosophises about a stone',
                published_date=timezone.datetime(1813, 1, 28),
                created_at=timezone.now(),
                updated_at=timezone.now()
            ),
            Book(
                title='Funny Daddy Shark Jokes Compilation',
                summary='Daddy SHARK DUDUDUDUDUDUDUDUDUD SHARK DUDUDUDUDUD SHARK DUDUDUDUD DADDY SHARK',
                published_date=timezone.datetime(1813, 1, 28),
                created_at=timezone.now(),
                updated_at=timezone.now()
            ),
            Book(
                title='Making fun of my traumatic childhood and I stop when I cry',
                summary='The title says it all guys! Hahaha I wish i didnt have Ligma...',
                published_date=timezone.datetime(1813, 1, 28),
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
        ]
        Book.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS('Successfully populated books.'))

        reviews = [
            Review(book=Book.objects.get(id=1), reviewer_name="John",
                   review_text="Great book, I loved the plot and characters!", rating=5, 
                   created_at=timezone.now(),
                   updated_at=timezone.now()),
            Review(book=Book.objects.get(id=2), reviewer_name="Sarah",
                   review_text="The story was a bit slow for me, but overall enjoyable.", rating=3,
                   created_at=timezone.now(),
                   updated_at=timezone.now()),
            Review(book=Book.objects.get(id=3), reviewer_name="Mike",
                   review_text="This book was a real page-turner, I couldn't put it down!", rating=4,
                   created_at=timezone.now(),
                   updated_at=timezone.now()),
            Review(book=Book.objects.get(id=4), reviewer_name="Emily",
                   review_text="I found the writing style a bit difficult to follow at times, but still a good read.", rating=3,
                   created_at=timezone.now(),
                   updated_at=timezone.now()),
            Review(book=Book.objects.get(id=5), reviewer_name="David",
                   review_text="One of the best books I've read in a long time, highly recommend!", rating=5,
                   created_at=timezone.now(),
                   updated_at=timezone.now()),
            Review(book=Book.objects.get(id=6), reviewer_name="Amy",
                   review_text="The characters felt a bit one-dimensional to me, but the plot was interesting.", rating=3,
                   created_at=timezone.now(),
                   updated_at=timezone.now()),
            Review(book=Book.objects.get(id=7), reviewer_name="Tom",
                   review_text="Not really my cup of tea, but I can see why others might enjoy it.", rating=2,
                   created_at=timezone.now(),
                   updated_at=timezone.now()),
            Review(book=Book.objects.get(id=8), reviewer_name="Kate",
                   review_text="I loved the way the author explored the themes of identity and belonging in this book.", rating=4,
                   created_at=timezone.now(),
                   updated_at=timezone.now()),
            Review(book=Book.objects.get(id=9), reviewer_name="Jake",
                   review_text="The pacing was a bit uneven, but the ending was satisfying.", rating=3,
                   created_at=timezone.now(),
                   updated_at=timezone.now()),
            Review(book=Book.objects.get(id=1), reviewer_name="Linda",
                   review_text="I found the characters to be unrealistic and unrelatable.", rating=2,
                   created_at=timezone.now(),
                   updated_at=timezone.now()),
        ]
        Review.objects.bulk_create(reviews)
        self.stdout.write(self.style.SUCCESS(
            'Successfully populated reviews.'))

        authors = Author.objects.all()
        books = Book.objects.all()
        authorships = [
            Authorship(author=authors[0], book=books[0],
                       contribution="Main Author", royalty_percentage=30.5),
            Authorship(author=authors[1], book=books[0],
                       contribution="Illustrator", royalty_percentage=15.0),
            Authorship(author=authors[0], book=books[1],
                       contribution="Co-Author", royalty_percentage=25.0),
            Authorship(author=authors[2], book=books[1],
                       contribution="Editor", royalty_percentage=10.0),
            Authorship(author=authors[3], book=books[2],
                       contribution="Translator", royalty_percentage=20.0),
            Authorship(author=authors[0], book=books[3],
                       contribution="Main Author", royalty_percentage=35.0),
            Authorship(author=authors[1], book=books[3],
                       contribution="Editor", royalty_percentage=12.5),
            Authorship(author=authors[4], book=books[4],
                       contribution="Co-Author", royalty_percentage=25.0),
            Authorship(author=authors[3], book=books[4],
                       contribution="Illustrator", royalty_percentage=15.0),
            Authorship(author=authors[2], book=books[5],
                       contribution="Main Author", royalty_percentage=30.0),
        ]
        Authorship.objects.bulk_create(authorships)
        self.stdout.write(self.style.SUCCESS(
            'Successfully populated authorships.'))
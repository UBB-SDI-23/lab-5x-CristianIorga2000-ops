import os
import random
import subprocess
from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()

NUM_AUTHORS = 10
NUM_BOOKS = 10
NUM_REVIEWS = 10
NUM_AUTHORSHIPS = 10
LOG_PROGRESS_EVERY = 100000

class Command(BaseCommand):
    help = 'Populate the database with sample data.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.populate_models()
        self.execute_sql_scripts()

    def populate_models(self):
        self.generate_authors()
        self.generate_books()
        self.generate_reviews()
        self.generate_authorships()
        self.stdout.write("All models successfully populated.")


    def execute_sql_scripts(self):
        db_settings = settings.DATABASES['default']
        host = db_settings['HOST']
        user = db_settings['USER']
        password = db_settings['PASSWORD']
        db_name = db_settings['NAME']

        os.environ['PGPASSWORD'] = password

        for filename in ('authors.sql', 'books.sql', 'reviews.sql', 'authorships.sql'):
            subprocess.run(f"psql -h {host} -U {user} -d {db_name} -f {filename}", shell=True, check=True)

        del os.environ['PGPASSWORD']

    def generate_authors(self):
        self.stdout.write("Generating authors...")
        with open("authors.sql", "w") as authors_file:
            for i in range(NUM_AUTHORS):
                name = fake.name().replace("'", "''")
                email = fake.email()
                bio = fake.text().replace("'", "''")
                authors_file.write(f"INSERT INTO app_author (name, email, bio, created_at, updated_at) VALUES ('{name}', '{email}', '{bio}', NOW(), NOW());\n")
                if (i + 1) % LOG_PROGRESS_EVERY == 0:
                    self.stdout.write(f"Generated {i + 1} authors")
        self.stdout.write("Authors successfully generated.")

    def generate_books(self):
        self.stdout.write("Generating books...")
        with open("books.sql", "w") as books_file:
            for i in range(NUM_BOOKS):
                title = fake.sentence().replace("'", "''")
                summary = fake.text().replace("'", "''")
                published_date = fake.date_between(start_date='-30y', end_date='today')
                books_file.write(f"INSERT INTO app_book (title, summary, published_date, created_at, updated_at) VALUES ('{title}', '{summary}', '{published_date}', NOW(), NOW());\n")
                if (i + 1) % LOG_PROGRESS_EVERY == 0:
                    self.stdout.write(f"Generated {i + 1} books")
        self.stdout.write("Books successfully generated.")

    def generate_reviews(self):
        self.stdout.write("Generating reviews...")
        with open("reviews.sql", "w") as reviews_file:
            for i in range(NUM_REVIEWS):
                book_id = random.randint(1, NUM_BOOKS)
                reviewer_name = fake.name().replace("'", "''")
                review_text = fake.text().replace("'", "''")
                rating = fake.random_int(min=1, max=5)
                reviews_file.write(f"INSERT INTO app_review (book_id, reviewer_name, review_text, rating, created_at, updated_at) VALUES ({book_id}, '{reviewer_name}', '{review_text}', {rating}, NOW(), NOW());\n")
                if (i + 1) % LOG_PROGRESS_EVERY == 0:
                    self.stdout.write(f"Generated {i + 1} reviews")
        self.stdout.write("Reviews successfully generated.")

    def generate_authorships(self):
        self.stdout.write("Generating authorships...")
        with open("authorships.sql", "w") as authorships_file:
            for i in range(NUM_AUTHORSHIPS):
                author_id = random.randint(1, NUM_AUTHORS)
                book_id = random.randint(1, NUM_BOOKS)
                contribution = fake.job().replace("'", "''")
                royalty_percentage = fake.random_number(digits=5, fix_len=True)
                authorships_file.write(f"INSERT INTO app_authorship (author_id, book_id, contribution, royalty_percentage) VALUES ({author_id}, {book_id}, '{contribution}', {royalty_percentage});\n")
                if (i + 1) % LOG_PROGRESS_EVERY == 0:
                    self.stdout.write(f"Generated {i + 1} authorships")
        self.stdout.write("Authorships successfully generated.")

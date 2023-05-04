import random
from django.core.management.base import BaseCommand
from faker import Faker
from app.models import Author, Book, Authorship

fake = Faker()

NUM_AUTHORSHIPS = 100

class Command(BaseCommand):
    help = 'Add 100 new authorship objects to the database.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.create_authorships()


    def create_authorships(self):
        self.stdout.write("Generating authorships...")
        with open("authorships.sql", "w") as authorships_file:
            for _ in range(NUM_AUTHORSHIPS):
                author_id = random.randint(1, 100)
                book_id = random.randint(1, 100)
                contribution = fake.job().replace("'", "''")
                royalty_percentage = round(fake.random.uniform(0, 100), 2)
                role = fake.job().replace("'", "''") 
                authorships_file.write(f"INSERT INTO app_authorship (author_id, book_id, contribution, royalty_percentage, role) VALUES ({author_id}, {book_id}, '{contribution}', {royalty_percentage}, '{role}');\n")
        self.stdout.write("Authorships successfully generated.")

# Generated by Django 4.1.7 on 2023-04-18 05:55

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_book_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorship',
            name='contribution',
            field=models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator(50)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date.today)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]

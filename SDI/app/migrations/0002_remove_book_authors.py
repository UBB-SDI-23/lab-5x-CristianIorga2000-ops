# Generated by Django 4.1.7 on 2023-03-20 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-25 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]

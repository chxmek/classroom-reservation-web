# Generated by Django 5.0.2 on 2024-03-26 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_book_time_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='time_period',
        ),
    ]
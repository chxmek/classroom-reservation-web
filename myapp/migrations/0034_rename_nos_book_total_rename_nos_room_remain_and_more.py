# Generated by Django 5.0.2 on 2024-03-26 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_rename_time_book_time_create_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='nos',
            new_name='total',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='nos',
            new_name='remain',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='rem',
            new_name='total',
        ),
    ]

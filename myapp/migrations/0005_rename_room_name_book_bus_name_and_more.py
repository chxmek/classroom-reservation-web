# Generated by Django 5.0.3 on 2024-03-15 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_bus_name_book_room_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='room_name',
            new_name='bus_name',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='room_name',
            new_name='bus_name',
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-15 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_dest_book_floor_rename_dest_bus_floor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='bus_name',
            new_name='room_name',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='bus_name',
            new_name='room_name',
        ),
    ]

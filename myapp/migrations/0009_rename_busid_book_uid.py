# Generated by Django 5.0.3 on 2024-03-16 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_room_name_book_bus_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='busid',
            new_name='uid',
        ),
    ]
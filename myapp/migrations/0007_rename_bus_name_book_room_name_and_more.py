# Generated by Django 5.0.3 on 2024-03-15 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_bus_name_bus_room_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='bus_name',
            new_name='room_name',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='room_name',
            new_name='bus_name',
        ),
    ]

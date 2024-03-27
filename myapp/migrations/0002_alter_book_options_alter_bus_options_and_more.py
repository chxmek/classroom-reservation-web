# Generated by Django 5.0.3 on 2024-03-15 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'List of Books'},
        ),
        migrations.AlterModelOptions(
            name='bus',
            options={'verbose_name_plural': 'List of Busses'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'List of Users'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='source',
            new_name='building',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='source',
            new_name='building',
        ),
    ]
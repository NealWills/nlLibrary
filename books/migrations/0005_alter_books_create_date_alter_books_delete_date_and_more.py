# Generated by Django 5.1.2 on 2024-11-09 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_books_options_books_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='create_date'),
        ),
        migrations.AlterField(
            model_name='books',
            name='delete_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='delete_date'),
        ),
        migrations.AlterField(
            model_name='books',
            name='is_delete',
            field=models.IntegerField(blank=True, default=0, verbose_name='is_delete'),
        ),
        migrations.AlterField(
            model_name='books',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='update_date'),
        ),
    ]
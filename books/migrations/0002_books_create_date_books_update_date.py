# Generated by Django 5.1.2 on 2024-11-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='create_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='create_date'),
        ),
        migrations.AddField(
            model_name='books',
            name='update_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='update_date'),
        ),
    ]
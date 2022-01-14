# Generated by Django 4.0.1 on 2022-01-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_avg_stars_bookstoreuser_review_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isbn',
            new_name='isbn13',
        ),
        migrations.RemoveField(
            model_name='book',
            name='editorial',
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='Penguin', max_length=100, verbose_name='Publisher'),
            preserve_default=False,
        ),
    ]
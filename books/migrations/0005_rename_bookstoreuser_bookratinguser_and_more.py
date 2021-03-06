# Generated by Django 4.0.1 on 2022-01-15 18:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0004_rename_isbn_book_isbn13_remove_book_editorial_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookStoreUser',
            new_name='BookRatingUser',
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn13',
            field=models.IntegerField(blank=True, null=True, verbose_name='ISBN13'),
        ),
    ]

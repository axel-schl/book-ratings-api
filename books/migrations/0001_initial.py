# Generated by Django 4.0.1 on 2022-01-14 03:16

import books.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('editorial', models.CharField(max_length=100, verbose_name='Editorial')),
                ('edition_year', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2022), django.core.validators.MinValueValidator(1900)], verbose_name='Edition Year')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('isbn', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(13), django.core.validators.MinLengthValidator(13)], verbose_name='ISBN')),
                ('image_thumbnail', models.ImageField(blank=True, null=True, upload_to=books.models.Book.path_to_book, verbose_name='Thumbnail Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author', verbose_name='Author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookgenre', verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'Book',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Stars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'book')},
                'index_together': {('user', 'book')},
            },
        ),
    ]

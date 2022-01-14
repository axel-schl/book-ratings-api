import uuid
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

import datetime

class BookStoreUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1),MaxValueValidator(5)])
    review = models.TextField(null=True, max_length=500)

class Meta:
        unique_together = ['book', 'user']
        ordering = ['book__title']



class Book(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, verbose_name="Title")
    author = models.ForeignKey('Author',related_name="author_books",verbose_name="Author", on_delete=models.CASCADE)
    publisher = models.CharField(max_length=100, verbose_name="Publisher")
    edition_year = models.PositiveIntegerField(verbose_name="Edition Year",validators=[MaxValueValidator(datetime.datetime.now().year), MinValueValidator(1900)])
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    isbn13 = models.IntegerField( null=True, blank=True, verbose_name="ISBN13")
    genre = models.ForeignKey('BookGenre',related_name="books_genres", verbose_name="Genre", on_delete=models.CASCADE) 
    avg_stars = models.FloatField(default=0.0, verbose_name="stars",validators=[MaxValueValidator(5.0)])
    
    def update_book_stars(sender, instance, **kwargs):
    
        stars = BookStoreUser.objects.filter(book=instance.book).exclude(stars__isnull=True)
        count_stars = stars.count()
        sum_stars = stars.aggregate(Sum('stars')).get('stars__sum')
    
        try:
            instance.book.avg_stars = round(sum_stars/count_stars, 2)
        except:
            pass
    
        instance.book.save()


    post_save.connect(update_book_stars, sender=BookStoreUser)

    def path_to_book(instance,filename):
        
        return f'books/{instance.id}/{filename}'

    image_thumbnail = models.ImageField(upload_to=path_to_book, null=True, blank=True, verbose_name="Thumbnail Image")
    
    
    class Meta:
        verbose_name = "Book"
        ordering = ['title']

  

    def __str__(self):
        return f'{self.title}, author: {self.author}'

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    bio = models.TextField(null=True, blank=True, verbose_name="Bio")
    
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)

class BookGenre(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Name", unique=True)
    slug = models.SlugField(
        unique=True)

    class Meta:
        verbose_name = "Genre"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BookGenre, self).save(*args, **kwargs)


    

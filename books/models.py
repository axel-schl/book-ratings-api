import uuid
from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime


class Star(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user','book'),)
        index_together = (('user','book'),)

class Book(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, verbose_name="Title")
    author = models.ForeignKey('Author',related_name="author_books",verbose_name="Author", on_delete=models.CASCADE)
    editorial = models.CharField(max_length=100, verbose_name="Editorial")
    edition_year = models.PositiveIntegerField(verbose_name="Edition Year",validators=[MaxValueValidator(datetime.datetime.now().year), MinValueValidator(1900)])
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    isbn = models.IntegerField( null=True, blank=True, verbose_name="ISBN")
    genre = models.ForeignKey('BookGenre',related_name="books_genres", verbose_name="Genre", on_delete=models.CASCADE) 
    

    def path_to_book(instance,filename):
        
        return f'books/{instance.id}/{filename}'

    image_thumbnail = models.ImageField(upload_to=path_to_book, null=True, blank=True, verbose_name="Thumbnail Image")
    
    
    class Meta:
        verbose_name = "Book"
        ordering = ['title']

    def n_reviews(self):
        reviews = Star.objects.filter(book=self)
        return len(reviews)

    def avg_stars(self):
        sum = 0
        reviews = Star.objects.filter(book=self)
        for review in reviews:
            sum += review.stars
        if len(reviews)>0:
            return sum/len(reviews)
        else:
            return 0

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


    

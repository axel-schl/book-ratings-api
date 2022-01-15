from rest_framework import serializers
from .models import Book, BookGenre, Author, BookRatingUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = '__all__'

    books = BookSerializer(many=True, source="books_genres")
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    books = BookSerializer(many=True, source="author_books")

class BookRatingUserSerializer(serializers.ModelSerializer):

    book = BookSerializer(read_only=True)

    class Meta:
        model = BookRatingUser
        fields = ['book', 'stars', 'review']
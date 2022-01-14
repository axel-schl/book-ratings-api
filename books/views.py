from rest_framework import viewsets
from .models import Book, BookGenre, Author
from .serializers import BookSerializer, BookGenreSerializer, AuthorSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    lookup_field = 'slug'  

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'slug'  
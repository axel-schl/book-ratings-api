from rest_framework import status,viewsets, views, filters, authentication, permissions
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.response import Response

from .models import Book, BookGenre, Author, BookRatingUser
from .serializers import BookSerializer, BookGenreSerializer, AuthorSerializer, BookRatingUserSerializer
from .paginators import ExtendedPagination

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'author','avg_stars']
    ordering_fields = ['title', 'author','avg_stars']
    filterset_fields = {
    'avg_stars': ['lte', 'gte'],  
    'author': ['exact'],      
}
    pagination_class = ExtendedPagination
    

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    lookup_field = 'slug'  

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'slug'  


class BookRatingUserViewSet(views.APIView):
    
    authentication_classes = [authentication.SessionAuthentication]  
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        queryset = BookRatingUser.objects.filter(user=self.request.user)
        serializer = BookRatingUserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, *args, **kwargs):
        try:
           book = Book.objects.get(id=request.data['uuid'])
        except Book.DoesNotExist:
            return Response(
                {'status': 'Book not found'},
                status=status.HTTP_404_NOT_FOUND)

      
        book_user, created = BookRatingUser.objects.get_or_create(
            user=request.user, book=book)

       
        
        book_user.stars = request.data.get('stars', -1)
        book_user.review = request.data.get('review', None)

        book_user.save()

        return Response(
            {'status': 'Saved'}, status=status.HTTP_200_OK)
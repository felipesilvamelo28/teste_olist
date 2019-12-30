from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from books.models import Book
from books.api.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    """
    Creating Books ViewSet.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    """
    Creating Search & Filter.
    """
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('id', 'name', 'publication_year')
    filter_fields = ('name', 'edition', 'publication_year', 'author')

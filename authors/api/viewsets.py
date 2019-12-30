from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from authors.models import Author
from authors.api.serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    """
    Creating Author ViewSet.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    """
    Creating Search & Filter.
    """
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('id', 'name')
    filter_fields = ('id', 'name')

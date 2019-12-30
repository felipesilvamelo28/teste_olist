from rest_framework.serializers import ModelSerializer
from books.models import Book
from authors.api.serializers import AuthorSerializer


class BookSerializer(ModelSerializer):
    """
    Creating Books Serializer.
    """
    """
    Creating the Nested Serializer for Authors.
    """
    author = AuthorSerializer(many=True)

    class Meta:
        """
        Model indication for the Serializer.
        """
        model = Book
        """
        Indicating fields in Serializer.
        """
        fields = ['id', 'name', 'edition', 'publication_year', 'author']
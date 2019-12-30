from rest_framework.serializers import ModelSerializer
from authors.models import Author


class AuthorSerializer(ModelSerializer):
    """
    Creating Author Serializer.
    """
    class Meta:
        """
        Model indication for the Serializer.
        """
        model = Author
        """
        Indicating fields in Serializer.
        """
        fields = ['id', 'name']

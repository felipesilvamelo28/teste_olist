from django.db import models


class Author(models.Model):
    """
    Creating Author Model.
    """
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

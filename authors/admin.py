from django.contrib import admin
from .models import Author


"""
Including Author Model in the Admin.
"""
admin.site.register(Author)

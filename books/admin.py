from django.contrib import admin
from .models import Book


"""
Including Book Model in the Admin.
"""
admin.site.register(Book)

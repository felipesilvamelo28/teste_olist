from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.api.viewsets import BookViewSet
from authors.api.viewsets import AuthorViewSet

"""
Creating router.
"""
router = routers.DefaultRouter()
"""
Creating router register of books.
"""
router.register(r'books', BookViewSet)
"""
Creating router register of authors.
"""
router.register(r'authors', AuthorViewSet)
"""
Including router in the urlpatterns.
"""
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

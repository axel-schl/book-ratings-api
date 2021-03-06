"""book_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

# Api router
router = routers.DefaultRouter()
from books import views as book_views


router = routers.DefaultRouter()
router.register('books', book_views.BookViewSet, basename='Book')
router.register('genres', book_views.GenreViewSet, basename='BookGenre')
router.register('authors', book_views.AuthorViewSet, basename='Author')
urlpatterns = [
    # Admin routes
    path('admin/', admin.site.urls),

    # Api routes
    path('api/', include('authentication.urls')), 
    path('api/', include(router.urls)),
    path('api/user_ratings/', book_views.BookRatingUserViewSet.as_view()),
]

if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
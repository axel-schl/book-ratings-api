from django.contrib import admin
from .models import Book, Author, BookGenre, Stars


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookGenre)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]

@admin.register(Stars)
class StarsAdmin(admin.ModelAdmin):
    pass
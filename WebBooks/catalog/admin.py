from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 'first_name'
    )

    fields = [
        'first_name', 'last_name',
        'date_of_birth', 'date_of_death'
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'genre', 'language', 'display_author'
    )

    list_filter = (
        'genre', 'author'
    )


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = (
        'book', 'status'
    )

    fieldsets = (
        ('A copy of the book', {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Status and termination', {
            'fields': ('status', 'due_back')
        }),
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)

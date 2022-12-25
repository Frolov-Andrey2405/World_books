from django.db import models
from django.urls import reverse

# Create your models here.


class Genre(models.Model):
    """To store information about book genres"""

    name = models.CharField(
        max_length=200,
        help_text='Enter a book genre',
        verbose_name='Book genre'
    )

    def __str__(self):
        return self.name


class Language(models.Model):
    """A guide to the languages in which the books are written"""

    name = models.CharField(
        max_length=200,
        help_text='Enter the language in which the book is written',
        verbose_name='Book language'
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    """To store information about the authors of books"""

    first_name = models.CharField(
        max_length=100,
        help_text='Enter the author\'s first name',
        verbose_name='Author\'s first name'
    )

    last_name = models.CharField(
        max_length=100,
        help_text='Enter the author\'s last name',
        verbose_name='Author\'s last name'
    )

    date_of_birth = models.DateField(
        help_text='Enter the author\'s date of birth',
        verbose_name='Date of birth',
        null=True,
        blank=True
    )

    date_of_death = models.DateField(
        help_text='Enter the author\'s date of death',
        verbose_name='Date of death',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    """Model for storing books"""

    title = models.CharField(
        max_length=200,
        help_text='Enter the title of the book',
        verbose_name='Book title'
    )

    genre = models.ForeignKey(
        'Genre',
        on_delete=models.CASCADE,
        help_text='Select a genre for the book',
        verbose_name='Book genre',
        null=True,
        blank=True
    )

    language = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE,
        help_text='Select the language in which the book is written',
        verbose_name='Book language',
        null=True,
        blank=True
    )

    author = models.ManyToManyField(
        'Author',
        help_text='Select the authors of the book',
        verbose_name='Book authors'
    )

    summary = models.TextField(
        max_length=1000,
        help_text='Enter a brief description or summary of the book',
        verbose_name='Book summary'
    )

    isbn = models.CharField(
        max_length=13,
        help_text='Enter the ISBN of the book (must contain 13 characters)',
        verbose_name='Book ISBN'
    )

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Authors'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Returns the URL to access a specific instance of the book
        return reverse('book-detail', args=[str(self.id)])


class Status(models.Model):
    """Model for storing book copy statuses"""

    name = models.CharField(
        max_length=20,
        help_text='Enter the status of the book copy (e.g. available, borrowed, etc.)',
        verbose_name='Book copy status'
    )

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    """Model for storing information about specific copies of books"""

    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        null=True
    )

    inv_nom = models.CharField(
        max_length=20,
        null=True,
        help_text='Enter the inventory number of the book copy',
        verbose_name='Inventory number'
    )

    imprint = models.CharField(
        max_length=200,
        help_text='Enter the publisher and year of publication for this book copy',
        verbose_name='Publisher and year of publication'
    )

    status = models.ForeignKey(
        'Status',
        on_delete=models.CASCADE,
        null=True,
        help_text='Select the current status of this book copy (e.g. available, borrowed, etc.)',
        verbose_name='Book copy status'
    )

    due_back = models.DateField(
        null=True,
        blank=True,
        help_text='Enter the date when this book copy is due to be returned (if applicable)',
        verbose_name='Return due date'
    )

    def __str__(self):
        return f'{self.inv_nom} {self.book} {self.status}'

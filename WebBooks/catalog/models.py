from django.db import models
from django.urls import reverse

# Create your models here.


class Genre(models.Model):
    '''To store information about book genres'''

    name = models.CharField(
        max_length=200,
        help_text='Enter book genre',
        verbose_name='Book genre')

    def __str__(self):
        return self.name


class Language(models.Model):
    '''A guide to the languages in which the books are written'''

    name = models.CharField(
        max_length=200,
        help_text='Enter the language of the book',
        verbose_name='The language of the book')

    def __str__(self):
        return self.name


class Author(models.Model):
    '''To store information about the authors of books'''

    first_name = models.CharField(
        max_length=100,
        help_text="Enter the author's first name",
        verbose_name="Author's first name")

    last_name = models.CharField(
        max_length=100,
        help_text="Enter the author's last name",
        verbose_name="Author's last name")

    date_of_birth = models.DateField(
        help_text="Enter date of birth",
        verbose_name="Date of birth",
        null=True,
        blank=True)

    date_of_death = models.DateField(
        help_text="Enter the date of death",
        verbose_name="Date of death",
        null=True,
        blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    '''Model for storing books'''

    title = models.CharField(
        max_length=200,
        help_text='Enter the title of the book',
        verbose_name='Book title'
    )

    genre = models.ForeignKey(
        'Genre',
        on_delete=models.CASCADE,
        help_text='Enter a genre for the book',
        verbose_name='Book genre',
        null=True
    )

    language = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE,
        help_text='Select the language of the book',
        verbose_name='The language of the book',
        null=True
    )

    author = models.ManyToManyField(
        'Author',
        help_text='Select the author of the book',
        verbose_name='Author of the book',
        null=True
    )

    summary = models.TextField(
        max_length=1000,
        help_text='Enter a brief description of the book',
        verbose_name='Book abstract'
    )

    isbn = models.CharField(
        max_length=13,
        help_text='Must contain 13 characters',
        verbose_name='ISBN of the book'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Returns the URL to access a specific instance of the book
        return reverse('book-detail', args=[str(self.id)])

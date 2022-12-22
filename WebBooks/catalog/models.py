from django.db import models
from django.urls import reverse

# Create your models here.


class MyModelName(models.Model):

    # Multiple fields
    my_field_name = models.CharField(
        max_length=20,
        help_text='No more than 20 characters')

    class Meta:
        '''Metadata'''
        ordering = ['-my_field_name']

    def get_absolute_url(self):
        '''Methods'''
        return reverse("model-detail-view", args=[str(self.id)])

    def __str__(self):
        '''String to represent the MyModelName object in the Admin site'''
        return self.field_name

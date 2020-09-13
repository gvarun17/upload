from django.db import models
from s3direct.fields import S3DirectField
import uuid

'''
class Car(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    year_of_manufacture = models.CharField(max_length=255, blank=False, null=False)
    price = models.CharField(max_length=255, blank=False, null=False)
    image = S3DirectField(dest='primary_destination', blank=True)
    video = S3DirectField(dest='primary_destination', blank=True)

    def __str__(self):
        """
        Return a string representation of the model instance
        """
        return f"{self.name} ({self.year_of_manufacture}) - {self.price}"
'''


class Photo(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    photo = models.FileField()
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=255)
    rating=models.FloatField(default=1)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

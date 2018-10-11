from django.db import models

class MovieChoice(models.Model):
    name = models.CharField(max_length=300)
    yearReleased = models.CharField(max_length=4)
    ageAllowed = models.CharField(max_length=2)
    genre = models.CharField(max_length=20)



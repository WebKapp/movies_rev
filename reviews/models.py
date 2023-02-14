from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    poster = 0
    description = models.TextField(max_lenght=3000)


class Review(models.Model):
    movie = 0
    stars = 0
    review_text = 0

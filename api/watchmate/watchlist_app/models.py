from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    description = models.TextField(blank=True, max_length=255)

    def __str__(self):
        return self.title
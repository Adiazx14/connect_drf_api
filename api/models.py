from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField()
    cover = models.ImageField()

    def __str__(self):
        return self.name
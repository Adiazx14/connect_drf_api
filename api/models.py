from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField()
    cover = models.ImageField()

    def __str__(self):
        return self.name

class Package(models.Model):
    title = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    destination = models.TextField()
    duration = models.CharField(max_length=200)
    valid_from = models.DateField()
    valid_to = models.DateField()
    price = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField(unique=True, max_length=300)

    def __str__(self):
        return self.email
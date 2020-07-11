from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField()


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ManyToManyField(Image)
    date = models.DateField()

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField()


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    date = models.DateField()

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()
    github_url = models.URLField()
    linkedin_url = models.URLField()
    twitter_url = models.URLField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message =models.TextField()
    def __str__(self):
        return self.name
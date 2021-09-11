from django.db import models
import jsonfield


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=56)
    username = models.CharField(max_length=56)
    email = models.EmailField()
    phone = models.CharField(max_length=56)
    website = models.CharField(max_length=56)
    address = jsonfield.JSONField()
    company = jsonfield.JSONField()


class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    body = models.TextField()

    class Meta:
        ordering = ['userId']

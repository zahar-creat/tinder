from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    video = models.FileField(upload_to="videos/")
    description = models.TextField(max_length=500)
    pitch_desk = models.FileField()


class Users(AbstractUser):
    company_type = models.TextField(max_length=15)


class List:
    no_list = models.ManyToManyField(Project, related_name="no_list")
    yes_list = models.ManyToManyField(Project, related_name="yes_list")


class Image:
    images = models.FileField()

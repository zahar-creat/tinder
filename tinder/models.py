from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    video = models.FileField(upload_to="videos/")
    description = models.TextField(max_length=500)
    import_images = models.FileField(upload_to="important_image/")
    pitch_desk = models.FileField(upload_to="pitchdeck/")


class Users(AbstractUser):
    clist = models.ManyToManyField(Project, through="Choise")


class Choice(models.Model):
    ctype = models.BooleanField(default=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    project = models.ForeignKey(Users, on_delete=models.CASCADE)


class Image(models.Model):
    images = models.FileField(upload_to="image/")
    startapp = models.ForeignKey(Project, on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    video = models.FileField(upload_to="videos/")
    description = models.CharField(max_length=500)
    pitch_desk = models.FileField(upload_to="pitchdeck/")


class Users(AbstractUser):
    choicelist = models.ManyToManyField(Project, through="Choice")
    investor = "Инвестор"
    user = "Пользователь"
    users_list = [(investor, "Инвестор"), (user, "Пользователь")]
    user_type = models.CharField(max_length=100, choices=users_list, default=investor)
    company = "Компания"
    private = "Частное лицо"
    fund = "Фонд"
    comp_list = [(company, "Компания"), (private, "Частное лицо"), (fund, "Фонд")]
    company_type = models.CharField(max_length=100, choices=comp_list, default=company)


class Choice(models.Model):
    choicetype = models.BooleanField(default=False)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Image(models.Model):
    images = models.FileField(upload_to="image/")
    startup = models.ForeignKey(Project, on_delete=models.CASCADE)

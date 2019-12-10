from django.db import models
from django.contrib.auth.models import AbstractUser


class Group(models.Model):
    groupname = models.CharField(max_length=256, primary_key=True)
    schedule = models.CharField(
        max_length=256, default='000000000000000000000000000000000000000000000000')


class User(AbstractUser):
    username = models.CharField(max_length=256, unique=True)
    student_id = models.CharField(max_length=14)
    schedule = models.CharField(max_length=256)
    groupname = models.CharField(max_length=256)

    USERNAME_FIELD = 'username'

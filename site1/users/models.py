from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    organization = models.TextField()
    avatar = models.ImageField()
    user = models.ForeignKey(
        User,
        unique=True,
        on_delete=models.CASCADE,
    )
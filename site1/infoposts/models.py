
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Root(models.Model):
    """Модель данных корневой страницы"""
    topic = models.TextField(max_length=40)
    text = models.TextField()
    optional = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Roots'
    )


from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class NewsModel(models.Model):
    """Модель основной ленты на главной странице"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name='Автор',
    )
    title_news = models.TextField(
        blank=True,
        verbose_name='Заголовок новости',
    )

    text = models.TextField(
        blank=True,
        verbose_name='Текст новости',
    )

    pub_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата публикации',
    )
    image = models.ImageField(
        blank=True,
        verbose_name='Изображение в новости',
        upload_to='infoposts',
    )

    class Meta:

        verbose_name = 'News'


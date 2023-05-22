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


class Starting_info(models.Model):
    """
    Модель стартовой информации:
    - План
    - Юр. вопросы
    - Маркетплэйсы
    - Сопровождение
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='start_posts',
        verbose_name='Автор',
    )
    pub_date = models.DateTimeField(auto_now=True, auto_created=True, verbose_name='Дата публикации')
    title = models.TextField(max_length=50, verbose_name="Заголовок поста")
    description = models.TextField(max_length=500, verbose_name="Описание поста")
    text = models.TextField(max_length=15000, verbose_name="Текст поста")
    content = models.FileField(verbose_name="Видеоматериал к посту")
# Generated by Django 4.2.1 on 2023-05-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoposts', '0003_alter_newsmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsmodel',
            options={'ordering': (['text'],), 'verbose_name': 'News'},
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст новости'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='infoposts', verbose_name='Изображение в новости'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='title_news',
            field=models.TextField(blank=True, verbose_name='Заголовок новости'),
        ),
    ]

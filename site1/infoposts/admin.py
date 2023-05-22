from django.contrib import admin
from .models import NewsModel, Starting_info


class StartAdmin(admin.ModelAdmin):
    """Модель Старт в админке"""
    list_display = ("pk", "author", "pub_date", "title", "description", "text", "content")
    list_filter = ('pub_date', 'title',)
    empty_value_display = '-пусто-'


admin.site.register(NewsModel)
admin.site.register(Starting_info, StartAdmin)

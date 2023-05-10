from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class CreationForm(UserCreationForm):
    """Модель создания нового юзера"""
    class Meta(UserCreationForm.Meta):
        model = User

        fields = ('first_name', 'last_name', 'username', 'email',)

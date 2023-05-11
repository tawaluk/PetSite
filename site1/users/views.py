from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from .forms import CreationForm
from django.views.generic.detail import DetailView


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('infoposts:root')
    template_name = 'users/signup.html'


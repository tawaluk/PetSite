from django.shortcuts import render
from django.http import HttpResponse
from .models import Root


def root(request):
    templates = 'infoposts/root.html'
    data_root = {
        'title': 'HSW',
        'new': Root.objects.all()

    }
    return render(request, template_name=templates, context=data_root)
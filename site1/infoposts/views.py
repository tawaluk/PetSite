from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NewsModel
from .forms import NewsForm
from django.contrib.auth.decorators import login_required


def root(request):
    templates = 'infoposts/root.html'
    data_root = {
        'title': 'HSW',
        'news': NewsModel.objects.all()

    }
    return render(request, template_name=templates, context=data_root)


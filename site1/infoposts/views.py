from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NewsModel
from .forms import NewsForm
from django.contrib.auth.decorators import login_required


def main(request):
    templates = 'infoposts/main.html'
    data_root = {'title': 'delaYdelo'}
    return render(request, template_name=templates, context=data_root)


def news_project(request):
    templates = 'infoposts/news-project.html'
    data_root = {
        'title': 'delaYdelo',
        'news': NewsModel.objects.all()

    }
    return render(request, template_name=templates, context=data_root)



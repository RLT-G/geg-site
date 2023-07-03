from django.shortcuts import render
from .models import ModelNews


def index(request):
    data = {'news': ModelNews.objects.all()}
    return render(request, 'news/index.html', data)

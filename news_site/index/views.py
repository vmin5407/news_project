from django.shortcuts import render
from . import models


# Create your views here.
def home_page(request):
    categories = models.NewsCategory.objects.all()
    news = models.News.objects.all()
    context = {
        'categories': categories,
        'news': news
    }
    return render(request, 'home.html', context)

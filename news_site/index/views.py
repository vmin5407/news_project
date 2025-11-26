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


def category_page(request, pk):
    category = models.NewsCategory.objects.get(id=pk)
    news = models.News.objects.filter(category=category)

    context = {
        'category': category,
        'news': news
    }
    return render(request, 'category.html', context)


def news_page(request, pk):
    news = models.News.objects.get(id=pk)
    context = {
        'news': news
    }

    return render(request, 'news.html', context)

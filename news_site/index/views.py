from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django import views

from .forms import NewsForm


# Create your views here.
def home_page(request):
    categories = models.NewsCategory.objects.all()
    news = models.News.objects.order_by('-added_date')
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


class Register(views.View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = forms.RegForm
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('/')


def create(request):
    error = ""
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Неверная форма"
    form = NewsForm()
    context = {'form': form,
               'error': error}
    return render(request, 'create.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')

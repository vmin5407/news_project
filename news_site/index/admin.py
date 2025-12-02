from django.contrib import admin
from .models import NewsCategory, News, SavedArticle

# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(News)
admin.site.register(SavedArticle)
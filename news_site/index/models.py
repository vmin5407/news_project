from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=32, verbose_name="Название категории")
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"


class News(models.Model):
    title = models.CharField(max_length=128, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    photo = models.ImageField(upload_to="media", verbose_name="Фото", blank=True, null=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name="Категория")
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "заголовок"
        verbose_name_plural = "заголовки"

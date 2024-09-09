from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)  # Заголовок новости
    summary = models.TextField()  # Краткое содержание новости
    image = models.URLField()  # URL изображения новости
    date = models.TextField()  # Дата публикации новости
    link = models.URLField()  # Ссылка на полную новость
    view_count = models.IntegerField(default=0)  # Количество просмотров новости

    class Meta:
        managed = False  # Отключение управления этой моделью через миграции Django
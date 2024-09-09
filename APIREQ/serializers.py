from rest_framework import serializers
from APIREQ.models import News

class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)  # Поле для заголовка новости
    summary = serializers.CharField()  # Поле для краткого содержания новости
    image = serializers.URLField()  # Поле для URL изображения новости
    date = serializers.CharField()  # Поле для даты публикации новости
    link = serializers.URLField()  # Поле для ссылки на полную новость
    view_count = serializers.IntegerField()  # Поле для количества просмотров новости
    like_count = serializers.IntegerField()  # Поле для количества лайков новости
    dislike_count = serializers.IntegerField()  # Поле для количества дизлайков новости
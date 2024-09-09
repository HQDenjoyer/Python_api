from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from APIREQ.serializers import NewsSerializer
import json

class AllNewsListView(ListAPIView):
    serializer_class = NewsSerializer  # Указание сериализатора для преобразования данных новостей
    pagination_class = PageNumberPagination  # Указание класса пагинации

    def get_queryset(self):
        # Путь к JSON файлу с новостями
        json_file_path = r'C:\Users\1\PycharmProjects\pythonProject13\news.json'
        try:
            # Открытие и чтение JSON файла
            with open(json_file_path, 'r', encoding='utf-8') as f:
                news_data = json.load(f)
                return news_data  # Возврат всех данных новостей
        except FileNotFoundError:
            return []  # Возврат пустого списка, если файл не найден

class LatestNewsListView(ListAPIView):
    serializer_class = NewsSerializer  # Указание сериализатора для преобразования данных новостей
    pagination_class = PageNumberPagination  # Указание класса пагинации

    def get_queryset(self):
        # Путь к JSON файлу с новостями
        json_file_path = r'C:\Users\1\PycharmProjects\pythonProject13\news.json'
        try:
            # Открытие и чтение JSON файла
            with open(json_file_path, 'r', encoding='utf-8') as f:
                news_data = json.load(f)
                return news_data[:20]  # Возврат последних 20 новостей
        except FileNotFoundError:
            return []  # Возврат пустого списка, если файл не найден
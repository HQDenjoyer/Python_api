from urllib.parse import unquote

from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import logging

logger = logging.getLogger(__name__)

class NewsDetailView(APIView):
    def get(self, request, news_title):
        decoded_title = unquote(news_title)  # Декодирование заголовка новости
        json_file_path = r'C:\Users\1\PycharmProjects\pythonProject13\news.json'
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                news_data = json.load(f)  # Загрузка данных из JSON файла
                news_item = next((news for news in news_data if news['title'] == decoded_title), None)
                if news_item:
                    # Увеличиваем счетчик просмотров
                    news_item['view_count'] = news_item.get('view_count', 0) + 1

                    # Перезаписываем данные в JSON-файл
                    with open(json_file_path, 'w', encoding='utf-8') as f_w:
                        json.dump(news_data, f_w, ensure_ascii=False, indent=4)

                    # Возвращаем HTML шаблон, передавая в него данные новости
                    return render(request, 'web/news_detail.html', {'news': news_item})
                return Response({'error': 'News not found'}, status=status.HTTP_404_NOT_FOUND)
        except FileNotFoundError:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)

class NewsListView(APIView):
    def get(self, request):
        json_file_path = r'C:\Users\1\PycharmProjects\pythonProject13\news.json'
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                news_data = json.load(f)  # Загрузка данных из JSON файла
                sort_by = request.GET.get('sort_by', 'none')
                if sort_by == 'views':
                    news_data = sorted(news_data, key=lambda x: x['view_count'], reverse=True)
                elif sort_by == 'likes':
                    news_data = sorted(news_data, key=lambda x: x['like_count'], reverse=True)
                elif sort_by == 'dislikes':
                    news_data = sorted(news_data, key=lambda x: x['dislike_count'], reverse=True)
                logger.info(f'Loaded {len(news_data)} news items from JSON')
                paginator = Paginator(news_data, 10)  # 10 новостей на страницу
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)

                context = {
                    'news_list': page_obj.object_list,
                    'previous_page': page_obj.previous_page_number() if page_obj.has_previous() else None,
                    'next_page': page_obj.next_page_number() if page_obj.has_next() else None,
                }
                return render(request, 'web/main_page.html', context)
        except FileNotFoundError:
            logger.error('JSON file not found')
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        except json.JSONDecodeError as e:
            logger.error(f'Error decoding JSON: {e}')
            return Response({'error': 'Error decoding JSON'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NewsReactionView(APIView):
    def post(self, request, news_title):
        decoded_title = unquote(news_title)  # Декодирование заголовка новости
        json_file_path = r'C:\Users\1\PycharmProjects\pythonProject13\news.json'
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                news_data = json.load(f)  # Загрузка данных из JSON файла
                news_item = next((news for news in news_data if news['title'] == decoded_title), None)
                if news_item:
                    reaction = request.data.get('reaction')
                    if reaction == 'like':
                        news_item['like_count'] += 1
                    elif reaction == 'dislike':
                        news_item['dislike_count'] += 1
                    with open(json_file_path, 'w', encoding='utf-8') as f:
                        json.dump(news_data, f, ensure_ascii=False, indent=4)
                    return Response({
                        'success': True,
                        'like_count': news_item['like_count'],
                        'dislike_count': news_item['dislike_count']
                    })
                return Response({'error': 'News not found'}, status=status.HTTP_404_NOT_FOUND)
        except FileNotFoundError:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        except json.JSONDecodeError as e:
            return Response({'error': 'Error decoding JSON'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

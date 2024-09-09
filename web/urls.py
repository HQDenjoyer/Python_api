from django.urls import path
from .views import NewsDetailView, NewsListView, NewsReactionView

urlpatterns = [
    path('<str:news_title>/', NewsDetailView.as_view(), name='news-detail'),  # URL для отображения деталей новости по заголовку
    path('', NewsListView.as_view(), name='main-page'),  # URL для главной страницы с списком новостей
    path('api/reaction/<str:news_title>/', NewsReactionView.as_view(), name='news-reaction'),  # URL для обработки реакций (лайки/дизлайки) на новость по заголовку
]
from django.urls import path
from .views import AllNewsListView, LatestNewsListView

urlpatterns = [
    path('allnews/', AllNewsListView.as_view(), name='all-news'),  # URL для отображения всех новостей
    path('news/', LatestNewsListView.as_view(), name='news'),  # URL для отображения последних новостей
]
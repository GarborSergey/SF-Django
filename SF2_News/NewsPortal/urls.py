from django.urls import path
from .views import NewsList, PostDetail, ArticlesList, home

app_name = 'news_portal'

urlpatterns = [
    path('', home, name='home'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('article/', ArticlesList.as_view(), name='articles_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
]
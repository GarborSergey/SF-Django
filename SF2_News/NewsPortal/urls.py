from django.urls import path
from .views import NewsList, PostDetail, ArticleList, home, PostCreate, PostSearch, PostDelete, PostUpdate

app_name = 'news_portal'

urlpatterns = [
    path('', home, name='home'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('articles/', ArticleList.as_view(), name='articles_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
    path('edit/<int:pk>', PostUpdate.as_view(), name='post_edit'),
]
# сори, но отдельно для новостей и статей, я адреса писать не буду, кушайте так))))00))0)
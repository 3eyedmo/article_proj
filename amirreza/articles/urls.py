from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('', views.show_articles, name='read_articles'),
    path('<int:article_id>/', views.article_detail, name='detail_article')
]

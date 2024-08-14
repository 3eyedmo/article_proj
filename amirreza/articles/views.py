from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article

def show_articles(request):
    articles = Article.objects.all()
    articles = list(articles)
    return render(
        request=request,
        template_name='articles/index.html',
        context= {'articles': articles}
    )

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(
        request=request,
        template_name='articles/detail.html',
        context={'article': article}
    )

## URLS:
# /articles
# /articles/{article.id} ==> view | path
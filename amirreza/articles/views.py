from django.shortcuts import render, redirect
from django.http import HttpResponse
from articles.models import Article
from .forms import ArticleForm


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

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:read_articles')
    elif request.method == "GET":
        form = ArticleForm()
    return render(
        request,
        template_name='articles/create.html',
        context={'form': form}
    )

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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

def login_required_(func):
    def decorator(request):
        if not request.user.is_authenticated:
            return redirect('articles:read_articles')

        return func(request)
    
    return decorator

@login_required_
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            article = Article(
                title=request.POST.get('title'),
                introduction=request.POST.get('introduction'),
                body=request.POST.get('body'),
                user=request.user
            )
            article.save()
            return redirect('articles:read_articles')
    elif request.method == "GET":
        form = ArticleForm()
    return render(
        request,
        template_name='articles/create.html',
        context={'form': form}
    )

@login_required
def view2(request):
    ##
    ...
    ###

@login_required
def view3(request):
    ##
    ...
    ###

@login_required
def view4(request):
    ##
    ...
    ###

# Request Methods:
# Read: GET
# Create: POST
# Update: PUT | PATCH
# Delete: DELETE


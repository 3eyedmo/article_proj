from django.contrib import admin
from articles.models import Article


# admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'introduction', 'body'
    ]

admin.site.register(Article, ArticleAdmin)
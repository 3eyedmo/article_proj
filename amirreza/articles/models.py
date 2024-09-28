from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model



class Article(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True) # author
    title = models.TextField()
    introduction = models.TextField()
    body = models.TextField()

    def get_absolute_url(self):
        return reverse("articles:detail_article", kwargs={"article_id": self.id})
    
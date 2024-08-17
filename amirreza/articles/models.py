from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.TextField()
    introduction = models.TextField()
    body = models.TextField()

    def get_absolute_url(self):
        return reverse("articles:detail_article", kwargs={"article_id": self.id})
    

    
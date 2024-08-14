from django.db import models



class Article(models.Model):
    title = models.TextField()
    introduction = models.TextField()
    body = models.TextField()

    
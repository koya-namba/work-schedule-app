from django.db import models

from staff.models import User


class Article(models.Model):
    """お知らせモデル"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='著者')
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

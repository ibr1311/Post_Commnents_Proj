from django.db import models
from django.contrib.auth import get_user_model

from comments.models import Comments

User = get_user_model()

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=55, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self, num=0):

        return f"From: '{self.author}', about: '{self.title}'"

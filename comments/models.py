from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'From: {self.author}, about {self.text}'
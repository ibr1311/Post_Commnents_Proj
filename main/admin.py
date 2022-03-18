from django.contrib import admin

from comments.models import Comments
from .models import Post

# Register your models here.
admin.site.register(Post)

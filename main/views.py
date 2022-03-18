from django.shortcuts import render

# Create your views here.
from main.models import Post


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'main/index.html', context=context)

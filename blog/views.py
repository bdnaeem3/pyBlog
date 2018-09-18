from django.shortcuts import render
from .models import Post


# Create your views here.
def home(response):
    return render(response, 'blog/home.html', {'posts': Post.objects.all()})


def about(response):
    return render(response, 'blog/about.html')

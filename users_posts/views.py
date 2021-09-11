from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class PostsView(ListView):
    """Список постов"""
    model = Post
    queryset = Post.objects.all()
    template_name = "index.html"

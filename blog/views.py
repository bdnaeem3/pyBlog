from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from rest_framework import viewsets

from .models import Post
from . import serializer, permissions


# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all()})


class AllPost(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']

    paginate_by = 5


class SinglePost(DetailView):
    model = Post


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        # return super().form_valid(form)
        return form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        # return super().form_valid(form)
        return form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class UserPost(ListView):
    model = Post

    # Template Stucture
    # <app>/<model>_<viewtype>.html

    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')


def about(request):
    return render(request, 'blog/about.html')


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = serializer.PostSerializer
    permission_classes = (permissions.PostAPIPermission,)
    queryset = Post.objects.all()
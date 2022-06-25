from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from blog.models import Post


class PostListView(ListView):
    """Class based view for displying list of blog posts"""
    model = Post


class PostCreateView(CreateView):
    """View for creating new blog post"""
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")


class PostDetailView(DetailView):
    """Displays details of a given post detail"""
    model = Post


class PostUpdateView(UpdateView):
    """View for updating matched blog post"""
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")


class PostDeleteView(DeleteView):
    """View for deleting matched blog post"""
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

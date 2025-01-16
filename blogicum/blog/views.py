from django.http import Http404
from django.shortcuts import get_object_or_404, render
from blog.models import Post


def index(request):
    template = "blog/index.html"
    posts_list = Post.objects.all()
    context = {
        "posts_list": posts_list,
    }
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    template = "blog/detail.html"
    context = {
        "post": post,
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = "blog/category.html"
    context = {
        "category": category_slug,
    }
    return render(request, template, context)

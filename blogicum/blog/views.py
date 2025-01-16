from django.http import Http404
from django.shortcuts import render


def index(request):
    template = "blog/index.html"
    context = {
        "posts": posts,
    }
    return render(request, template, context)


def post_detail(request, id):
    if id not in POSTS_BY_ID:
        raise Http404("Пост не найден")
    post = POSTS_BY_ID[int(id)]
    template = "blog/detail.html"
    context = {
        "post": post,
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = "blog/category.html"
    context = {
        "slug": category_slug,
    }
    return render(request, template, context)

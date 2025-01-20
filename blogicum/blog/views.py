from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from blog.models import Category, Post
from .constants import INDEX_PAGE_POSTS_LIMIT


def index(request):
    template = "blog/index.html"
    posts_list = Post.objects.filter(
        pub_date__lte=now(), is_published=True, category__is_published=True
    )[:INDEX_PAGE_POSTS_LIMIT]
    context = {
        "posts_list": posts_list,
    }
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        pk=id,
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True,
    )
    template = "blog/detail.html"
    context = {
        "post": post,
    }
    return render(request, template, context)


def category_posts(request, slug):
    template = "blog/category.html"
    category = get_object_or_404(Category, slug=slug, is_published=True)
    posts_list = category.posts.filter(
        is_published=True, pub_date__lte=now()
    )
    context = {
        "category": category,
        "posts_list": posts_list,
    }
    return render(request, template, context)

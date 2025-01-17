from django.http import Http404
from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category
from django.utils.timezone import now


def index(request):
    template = "blog/index.html"
    posts_list = Post.objects.filter(
        pub_date__lte=now(), is_published=True, category__is_published=True
    ).order_by("-pub_date")[:5]
    context = {
        "posts_list": posts_list,
    }
    return render(request, template, context)


def post_detail(request, id):
    try:
        post = Post.objects.get(pk=id)
        if (
            post.pub_date > now()
            or not post.is_published
            or not post.category.is_published
        ):
            raise Http404("Публикация недоступна")
    except Post.DoesNotExist:
        raise Http404("Публикация не найдена")
    template = "blog/detail.html"
    context = {
        "post": post,
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = "blog/category.html"
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=now()
    ).order_by('-pub_date')
    context = {
        "category": category,
        "posts_list": posts_list,
    }
    return render(request, template, context)

from django.shortcuts import render
from django.http import HttpResponse, Http404
from blog_posts.models import BlogPost


# Create your views here.
def index(request):
    posts = BlogPost.objects.all()[0:3]
    return render(
        request,
        "blog_posts/index.html",
        {
            "title": "Index",
            "posts": posts,
        },
    )


def all_posts(request):
    posts = BlogPost.objects.all()
    return render(
        request,
        "blog_posts/all_posts.html",
        {
            "title": "Blog Posts",
            "posts": posts,
        },
    )


def get_post(request, post):
    posts = BlogPost.objects.all()
    for blog_post in posts:
        if blog_post.id == int(post):
            return render(
                request,
                "blog_posts/post.html",
                {
                    "title": blog_post.title,
                    "post": blog_post,
                },
            )
    raise Http404("Post not found.")

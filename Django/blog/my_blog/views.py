from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "my_blog/index.html", {})


def all_posts(request):
    return render(request, "my_blog/all_posts.html", {})


def blog_post(request):
    return render(request, "my_blog/blog_post.html", {})

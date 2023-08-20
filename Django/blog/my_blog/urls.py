from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.all_posts, name="all_posts"),
    path("posts/<slug:slug>", views.blog_post, name="blog_post"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.all_posts, name="posts"),
    path("posts/<slug:slug>", views.get_post, name="blog_post"),
]

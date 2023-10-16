from django.shortcuts import render
from django.http import HttpResponse, Http404
from blog_posts.models import BlogPost

dummy_blog_posts = [
    {
        "url": "1",
        "title": "Understanding the Basics of Quantum Computing",
        "content": "Quantum computing is an area of study focused on the development of computer based technologies centered around the principles of quantum theory. Quantum computers use the quantum-mechanical phenomena of superposition and entanglement to perform operations on data...",
        "author": "Alice Smith",
        "date_posted": "2023-10-12",
    },
    {
        "url": "2",
        "title": "A Deep Dive into Neural Networks",
        "content": "Neural networks are a set of algorithms, modeled loosely after the human brain, that are designed to recognize patterns. They interpret sensory data through a kind of machine perception, labeling, and clustering of raw input...",
        "author": "John Doe",
        "date_posted": "2023-09-25",
    },
    {
        "url": "3",
        "title": "The Future of Artificial Intelligence: Opportunities and Challenges",
        "content": "The field of artificial intelligence (AI) has seen rapid advancements in the last decade. From self-driving cars to AI-powered chatbots, the technology is impacting almost every sector. But what does the future hold? In this blog post, we will explore...",
        "author": "Jane Doe",
        "date_posted": "2023-09-15",
    },
    {
        "url": "4",
        "title": "Augmented Reality vs. Virtual Reality: What’s the Difference?",
        "content": "Augmented reality (AR) and virtual reality (VR) are two of the most exciting technologies in the tech world. While they both offer immersive experiences, they do so in different ways and for different purposes. In this article, we’ll break down the key differences...",
        "author": "Bob Brown",
        "date_posted": "2023-08-30",
    },
]


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

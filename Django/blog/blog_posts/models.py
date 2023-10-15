from django.db import models


class BlogPost(models.Model):
    id = models.CharField(
        max_length=255, unique=True
    )  # unique=True ensures no two blog posts can have the same URL
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    date_posted = models.DateField()

    def __str__(self):
        return self.title

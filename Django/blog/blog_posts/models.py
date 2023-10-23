from django.db import models
from django.utils.text import slugify
from faker import Faker
from datetime import datetime, timedelta
import random


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    date_posted = models.DateField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


def generate_blogposts(num=10):
    """
    Generate 'num' number of BlogPost entries.
    """
    fake = Faker()

    for _ in range(num):
        title = fake.sentence(nb_words=5)
        content = fake.text()
        author = fake.name()
        # Generate a random date between now and a year ago
        days_old = random.randint(0, 365)
        date_posted = datetime.now() - timedelta(days=days_old)

        blog_post = BlogPost(
            title=title, content=content, author=author, date_posted=date_posted
        )

        blog_post.save()  # The slug will be generated in the overridden save() method

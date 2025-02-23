from datetime import date

from django.shortcuts import render

posts_data = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Diya",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": """
There's nothing like the views you get when hiking in the mountains
        """,
        "content": """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet
temporibus dolorum beatae saepe excepturi laboriosam in voluptate laudantium,
quisquam quae nisi deleniti itaque aperiam quaerat.
"""
    },
    {
        "slug": "coding-is-fun",
        "image": "coding.jpg",
        "author": "Diya",
        "date": date(2022, 8, 21),
        "title": "Coding is Fun",
        "excerpt": """
Coding can be fun if you love it properly!
        """,
        "content": """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet
temporibus dolorum beatae saepe excepturi laboriosam in voluptate laudantium,
quisquam quae nisi deleniti itaque aperiam quaerat.
"""
    },
    {
        "slug": "woods",
        "image": "woods.jpg",
        "author": "Diya",
        "date": date(2020, 1, 5),
        "title": "The Woods",
        "excerpt": """
Have you have thought about living in the woods?
        """,
        "content": """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet
temporibus dolorum beatae saepe excepturi laboriosam in voluptate laudantium,
quisquam quae nisi deleniti itaque aperiam quaerat.
"""
    }
]


def get_date(post):
    return post.get('date')


# Create your views here.


def index(request):
    sorted_posts = sorted(posts_data, key=get_date)
    latest_posts = sorted_posts[-3:]
    
    context = {
        "posts": latest_posts
    }
    return render(request, 'blog/index.html', context)


def posts(request):
    context = {
        "posts": posts_data
    }
    return render(request, 'blog/all-posts.html', context)


def single_post(request, slug):
    try:
        post = next(post for post in posts_data if post['slug'] == slug)
    except Exception:
        pass
    context = {
        "post": post
    }
    return render(request, 'blog/single-post.html', context)

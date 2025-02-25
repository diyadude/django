from django.shortcuts import render, get_object_or_404

from .models import Post


def get_date(post):
    return post.date


# Create your views here.


def index(request):
    posts_data = Post.objects.all()
    sorted_posts = sorted(posts_data, key=get_date)
    latest_posts = sorted_posts[-3:]
    
    context = {
        "posts": latest_posts
    }
    return render(request, 'blog/index.html', context)


def posts(request):
    posts_data = Post.objects.all().order_by('-date')
    context = {
        "posts": posts_data
    }
    return render(request, 'blog/all-posts.html', context)


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post,
        "tags": post.tags.all()
    }
    return render(request, 'blog/single-post.html', context)

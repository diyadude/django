from django.shortcuts import render
from django.views.generic import DetailView, ListView

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


class Posts(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ['-date']
    context_object_name = "posts"


class SinglePost(DetailView):
    template_name = "blog/single-post.html"
    model = Post

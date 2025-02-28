from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import CommentForm


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


class SinglePost(View):
    template_name = "blog/single-post.html"
    model = Post
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comments = post.comments.all().order_by("-id")
        context = {
            "post": post,
            "form": CommentForm(),
            "comments": comments
        }
        return render(request, "blog/single-post.html", context)
    
    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        comments = post.comments.all().order_by("-id")
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return HttpResponseRedirect(
                reverse('blog-single-post', args=[slug])
            )
        
        context = {
            "post": post,
            "form": form,
            "comments": comments
        }
        return render(request, "blog/single-post.html", context)

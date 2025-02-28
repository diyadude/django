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
    
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')
        read_later_status = post_id in stored_posts
        
        return read_later_status
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comments = post.comments.all().order_by("-id")
        context = {
            "post": post,
            "form": CommentForm(),
            "comments": comments,
            "saved_for_later": self.is_stored_post(request, post.id)
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
            "comments": comments,
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/single-post.html", context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        print(stored_posts)
        
        context = {}
        
        if not stored_posts:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            # posts = []
            # for post_id in stored_posts:
            #     posts.append(Post.objects.filter(id=post_id))
            context['posts'] = posts
            context['has_posts'] = True
        print(context)
        return render(request, 'blog/stored-posts.html', context)
        
    def post(self, request):
        stored_posts = request.session.get('stored_posts')
        
        if not stored_posts:
            stored_posts = []
        
        post_id = int(request.POST['post_id'])
        
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
        request.session['stored_posts'] = stored_posts
        post_slug = Post.objects.get(id=post_id).slug
        
        return HttpResponseRedirect(reverse("blog-single-post", args=[post_slug]))

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('posts/', views.Posts.as_view(), name='blog-posts'),
    path(
        'posts/<slug:slug>', views.SinglePost.as_view(), name='blog-single-post'
        ),  # /posts/my-first-post/
    path('read-later/', views.ReadLaterView.as_view(), name='read-later')
]

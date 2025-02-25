from django.urls import path

from . import views

urlpatterns = [
    # path('', views.review, name='review-page'),
    path('', views.ReviewView.as_view()), 
    # path('thank-you/', views.thank_you)
    path('thank-you', views.ThanksView.as_view()),
    path('reviews', views.ReviewsListView.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(),
         name="review-detail")
]

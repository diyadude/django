from django.urls import path

from . import views

urlpatterns = [
    # path('', views.review, name='review-page'),
    path('', views.ReviewView.as_view()), 
    path('thank-you/', views.thank_you)
]

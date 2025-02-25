from django.urls import path

from . import views

urlpatterns = [
    path('', views.review, name='review-page'),
    path('thank-you/', views.thank_you)
]

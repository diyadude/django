from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /challenges/
    path('<int:month>/', views.monthly_challenge_numric),
    path('<str:month>/', views.monthly_challenge, name='month-challenge')
]

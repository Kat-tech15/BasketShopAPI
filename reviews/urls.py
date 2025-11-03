from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.ReviewList.as_view()),
]
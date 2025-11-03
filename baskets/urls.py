from django.urls import path 
from . import views

urlpatterns = [
    path('list/', views.BasketList.as_view()),
    path('<int:pk>/', views.BasketDetail.as_view()),
]
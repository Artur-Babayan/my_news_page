from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:pk>/', views.category, name='category'),
    path('article/<int:pk>/', views.news_detail, name='news_detail'),
]

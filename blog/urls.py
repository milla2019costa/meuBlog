from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('meu_blog', views.meu_blog, name='meu_blog'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),


]

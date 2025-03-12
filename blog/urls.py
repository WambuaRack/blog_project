from django.urls import path 
from . import views

url_patterns=[
     path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
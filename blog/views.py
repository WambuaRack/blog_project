from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import post  # ✅ Use uppercase 'Post' to match the model name

def post_list(request):
    posts = post.objects.all().order_by('-date_posted')  # ✅ Changed 'post' to 'Post'
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):

  
    return render(request, "blog/post_detail.html", {"post": post})

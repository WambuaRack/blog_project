from django.shortcuts import render,get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse 
from . models import post 

def post_list(request):
    posts=post.objects.all().order_by('date_posted')
    return render(request,'blog/post_list.html',{'post':post})


def post_detail(request):
    post=get_list_or_404(post,post_id)
    return render(request,'blog/post_list.html',{'post':post})

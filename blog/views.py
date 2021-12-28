from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone
def post_list(request):
    posts = Post.objects.filter().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

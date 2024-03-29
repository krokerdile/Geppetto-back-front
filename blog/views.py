from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

# Create your views here.
from .models import Blog
from django.utils import timezone

def main(request):
    return render(request, 'main.html')

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()

# 제페토 되기 페이지
def be_geppetto(request):
    blogs=Blog.objects.all().order_by('-id')
    return render(request, 'be/be_geppetto.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'be/detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'be/new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.writer=request.user.username
    blog.name=request.user.profile.name
    blog.phone=request.user.profile.phone
    blog.age=request.GET['age']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/be_geppetto/'+str(blog.id))

def edit(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'be/edit.html',{'blog':blog})

def update(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    blog.title=request.GET['title']
    blog.writer=request.user.username
    blog.name=request.user.profile.name
    blog.phone=request.user.profile.phone
    blog.age=request.GET['age']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/be_geppetto/'+str(blog.id))

def delete(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('be_geppetto')
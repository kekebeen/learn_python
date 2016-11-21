from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.

def post_create(request):
    #instantiate new form with data
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form
    }
    return render(request, 'post_create.html', {'form': form})

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    return render(request, 'details.html',{'post': instance})

def post_list(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts': posts})

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
        "instance": instance,
        "title": instance.title
    }
    return render(request,'post_create.html', context)

def post_delete(request):
    return HttpResponse('<h1>Hello post create</h1>')
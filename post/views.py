from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Models for view
from .models import Post

# Forms for view
from .forms import PostForm

# Create your views here.

def get_all_posts(request):
    all_posts = Post.objects.filter(active=True)
    context = {
        'all_posts': all_posts,
        'title': 'Homepage',
    }

    return render(request, 'posts/index.html', context)

def get_post(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        'post': post,
        'title': 'Detailed Post',
    }

    return render(request, 'posts/detail.html', context)

def save_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.user = request.user
            temp_form.save()
            messages.add_message(request, messages.SUCCESS, 'Post Added Successfully.')
            return redirect('/')

    else:
        form = PostForm()

    context = {
        'form': form,
        'title': 'Add Post',
    }

    return render(request, 'posts/create.html', context)

def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.user = request.user
            temp_form.save()
            messages.add_message(request, messages.SUCCESS, 'Post Edited Successfully.')
            return redirect('/')

    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'title': 'Edit Post',
    }

    return render(request, 'posts/edit.html', context)

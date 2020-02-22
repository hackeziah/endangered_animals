from django.shortcuts import render
from pprint import pprint
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from django.core.files.storage import FileSystemStorage
from .forms import PostForm

import os
import datetime

# Create your views here.


def index(request):
    template = 'index.html'
    return render(request, template)


def gallery(request):
    template = 'gallery.html'
    return render(request, template)


def blog(request):  # view_all_Blog by users
    posts = Post.objects.filter(status=0)
    template = 'blog.html'
    context = {
        'posts': posts,  # same always
    }
    return render(request, template, context)


def view_single(request, post_id):
    single_post = Post.objects.get(id=int(post_id))
    comments = Comment.objects.filter(post=int(post_id))

    context = {
        'single_post': single_post,  # same always
        'comments': comments,  # same always
    }
    template = 'single.html'
    return render(request, template, context)

# def view_comments(request,post_id):
#     comments = Comment.objects.get(post = int(post_id))
#     context = {
#          'single_post': single_post, #same always
#             #  'comments': comments,
#     }
#     return render(request,template,context)


def view_all_posts(request):  # view_all_Post->For all Blog view by Admin
    posts = Post.objects.all()
    template = 'blog-colllection.html'
    context = {
        'posts': posts,  # same always
    }
    return render(request, template, context)


def contacts_us(request):
    template = 'contact.html'
    return render(request, template)


def add_personal_post(request):
    template = 'add-new-blog.html'
    return render(request, template)


def view_add_blog(request):
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add-new-blog.html', context)


def add_new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            m = Post()
            m.image = form.cleaned_data['image']
            m.content = form.cleaned_data['content']
            m.title = form.cleaned_data['title']
            m.created_by = form.cleaned_data['created_by']
            m.status = 0
            m.date_posted = True
            m.save()
    # make an else for validation
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def adding_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            m = Post()
            m.image = form.cleaned_data['image']
            m.content = form.cleaned_data['content']
            m.title = form.cleaned_data['title']
            m.created_by = form.cleaned_data['created_by']
            m.status = 0
            m.date_posted = True
            m.save()
    else:
        return HttpResponseRedirect(reverse_lazy('animals:blog-colllection'))
    return HttpResponseRedirect(reverse_lazy('animals:blog-colllection'))


def update_post_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            mYid = request.POST['id']
            m = Post.objects.get(id=int(mYid))
            m.image = form.cleaned_data['image']
            m.content = form.cleaned_data['content']
            m.title = form.cleaned_data['title']
            m.created_by = form.cleaned_data['created_by']
            m.status = request.POST['status']
            # m.date_posted = True
            m.save()
    else:
        return HttpResponseRedirect(reverse_lazy('animals:blog-colllection'))
    return HttpResponseRedirect(reverse_lazy('animals:blog-colllection'))


def view_single_blog(request, post_id):
    template = "view-post.html"
    data = Post.objects.get(id=int(post_id))
    context = {
        'data': data
    }
    return render(request, template, context)


def add_post(request):
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add-post.html', context)


def update_status(request):
    if request.method == 'POST':
        mYid = request.POST['id']
        stat = Post.objects.get(id=int(mYid))
        # stat.status = form.cleaned_data['status']
        stat.save()
    else:
        return HttpResponseRedirect(reverse_lazy('animals:blog-collections'))
    return HttpResponseRedirect(reverse_lazy('animals:blog-collections'))


def update_post_list(request, post_id):
    template = "update-post.html"
    post_info = Post.objects.get(id=int(post_id))
    context = {
        'post_info': post_info
    }
    return render(request, template, context)


def delete_post(request, post_id):
    # template = "blog-collection.html"
    post_info = Post.objects.get(id=int(post_id))
    post_info.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def add_comment(request):
    post = request.POST["post"]
    commented_by = request.POST["commented_by"]
    comment = request.POST["comment"]
    info_comment = Comment(
        post=post, commented_by=commented_by, comment=comment)
    info_comment.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def delete_comment(request, comment_id):
    template = "single.html"
    comment = Comment.objects.get(id=int(comment_id))
    comment.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

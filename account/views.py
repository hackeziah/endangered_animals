from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from .models import Account
# from ..models import Post
from django.http import HttpResponse, HttpResponseRedirect


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registrations.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    context = {}

    user = request.user  # paalam kung ano kung sino ung user na to
    if user.is_authenticated:  # checking of user
        return redirect('animals:blog-colllection')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('animals:blog-colllection')

    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form

    return render(request, "login.html", context)


# class for UpdateAccounts

def account_view(request):

    if not request.user.is_authenticated:
        return redirect("login-view")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
            # form.clear()
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context['account_form'] = form

    # blog_posts = Post.objects.filter(author=request.user)
    # context['blog_posts'] = blog_posts

    return render(request, "updateaccounts.html", context)

from django.shortcuts import render, redirect
# from django.http import HttpRequest
from django.contrib.auth import login, logout
from .models import Genre, Book, NewsEmail
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .sutility import get_client_ip
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .forms import *
from django import forms
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == 'POST':
        ip = get_client_ip(request)

        news_email = NewsEmail()
        news_email.ip = ip
        news_email.email = request.POST['email']
        news_email.save()
        return redirect('home')
    else:
        data = dict()
        data['genres'] = Genre.objects
        data['number_of_users'] = User.objects.count()
        data['number_of_books'] = Book.objects.count()

        return render(request, 'home.html', data)


def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, password=password)
            user.first_name = firstname
            user.save()
            login(request, user)
            return redirect('/')
    return render(request, 'register.html')


def signin(request):
    if request.method == 'POST':
        print('method is post')
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('form is valid')
            user = form.get_user()
            login(request, user)
            print('loged in')
            return redirect('/')
    return render(request, 'login.html')


def signout(request):
    if request.method == 'POST':
        logout(request)
        # return redirect('/')
        return redirect('/')

    return render(request, 'logout.html')


def genre_book_list(request, slug):
    genre = Genre.objects.get(slug=slug)
    all_book = Book.objects.filter(genre__in=[genre])
    context = {
        'books': all_book,
        'genre': genre
    }
    return render(request, 'books.html', context)


@login_required(login_url='/login/')
def file_attach(request):
    form = fileAttach()
    context = {
        'form': form,
    }
    if request.POST:
        form = fileAttach(request.POST, request.FILES)
        if form.is_valid():
            new_obj = form.save(commite=False)
            new_obj.save(user=request.user)
        return render(request, 'file-attachment.html', context=context)
    return render(request, 'file-attachment.html', context=context)

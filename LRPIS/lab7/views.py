from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('sign_out')
        return render(request, 'sign_in.html', {})
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(type(user))
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            form = {"username": username, "password": password, "errror": True}
            return render(request, 'sign_in.html', {'form': form})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def sign_up(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('sign_out')
        return render(request, 'sign_up.html', {})
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        form = {'username': username, 'password': password, 'email':email, "errors": []}
        if not username or User.objects.filter(username=username).count() != 0:
            form["errors"].append("Пользователь с таким именем уже существует" if username else "Не указано имя пользователя")
        if not password:
            form["errors"].append("Не указан пароль")
        if email and User.objects.filter(email=email).count() != 0:
            form["errors"].append("Пользователь с такой почтой уже существует")

        form["errors_count"] = len(form["errors"])

        if len(form["errors"]) == 0:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('archive')
        else:
            print(form)
            return render(request, 'sign_up.html', {'form': form})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def sign_out(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'sign_out.html', {})
        else:
            return redirect('sign_in')
    elif request.method == "POST":
        logout(request)
        return redirect("archive")
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

from .models import Article
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseForbidden

def groupmates(request):
    return render(request, 'groupmates.html')

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise HttpResponseNotFound

def new_article(request):
    if request.user.is_anonymous:
        return HttpResponseForbidden()

    if request.method == "GET":
        return render(request, 'create_article.html', {})
    elif request.method == "POST":
        form = {'text': request.POST["text"].strip(), 'title': request.POST["title"], "errors": []}

        if not form["title"]:
            form["errors"].append("Не указано имя статьи")
        if form["title"] and Article.objects.filter(title=form["title"]).count() > 0:
            form["errors"].append("Имя статьи должно быть уникальным")
        if not form["text"]:
            form["errors"].append("Статья не может быть пустой")
        form["errrors_count"] = len(form["errors"])

        if len(form["errors"]) == 0:
            article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
            return redirect('get_article', article_id=article.id)
        else:
            return render(request, 'create_article.html', {'form': form})

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

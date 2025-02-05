from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models
from datetime import datetime


# Create your views here.
def index(request):
    context = {}
    all = models.TitleModel.objects.all()
    context = {"all_task": all}
    return render(request, "wordlist/index.html", context)


def create(repuest):
    new_title = models.TitleModel()
    new_title.title = repuest.POST.get("title")
    new_title.save()
    return HttpResponseRedirect(reverse("wordlist:index"))


def delete(request):
    title_id = request.POST.get("title_id")
    action = request.POST.get("action")  # どのボタンが押されたか判定

    if action == "delete":
        # DELETE処理
        title = models.TitleModel.objects.get(id=title_id)
        title.delete()

    elif action == "update":
        # UPDATE処理
        new_title = request.POST.get("new_title")  # フォームから新しいタイトルを取得
        if new_title:  # 空でない場合のみ更新
            title = models.TitleModel.objects.get(id=title_id)
            title.title = new_title
            title.save()

    return HttpResponseRedirect(reverse("wordlist:index"))


def input(request, id):
    task = models.TitleModel.objects.get(id=id)
    context = {"task": task}
    return render(request, "wordlist/input.html", context)


def add_post(request, id):
    task = models.TitleModel.objects.get(id=id)

    if request.method == "POST":
        new_post = models.PostModel(
            title=task,
            date=request.POST.get("date"),
            page_number=request.POST.get("page_number"),
            content=request.POST.get("content"),
        )
        new_post.save()

    return HttpResponseRedirect(reverse("wordlist:input", args=[id]))


def delete_post(request, post_id):
    post = models.PostModel.objects.get(id=post_id)
    task_id = post.title.id  # 削除後にリダイレクトするために task_id を取得
    post.delete()
    return HttpResponseRedirect(reverse("wordlist:input", args=[task_id]))


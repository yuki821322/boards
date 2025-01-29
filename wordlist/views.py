from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models


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

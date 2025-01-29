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
    new_title = models.TitleModel.objects.get(id=title_id)
    new_title.delete()
    return HttpResponseRedirect(reverse("wordlist:index"))


# def change(reqest):
#     title_id = request.POST.get("title_id")
#     new_title = models.TitleModel.objects.get(id=title_id)
#     new_title = get_object_or_404(TitleModel, pk=new_title_id)
#     new_title.save()
#     return redirect("dxf_list")

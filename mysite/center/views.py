from django.shortcuts import render
from center.models import Center
from center import forms

from django.http import HttpResponseRedirect,Http404
from django.urls import reverse

# Create your views here.

def center_list(request):
    object = Center.objects.all()
    context = {
        "center" : object
    }
    return render(request,"./center/center_list.html",context)

def center_detail(request,id):
    object = Center.objects.get(id=id)
    context = {
        "center" : object
    }
    return render(request,"./center/center_detail.html",context)

def center_create(request):
    if request.method == "POST":
        form = forms.CenterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse("center:center_list"))
        else:
            context = {
                "form" : form
            }
            return render(request,"./center/center_create.html",context)
    context = {
            "form" : forms.CenterForm()
        }
    return render(request,"./center/center_create.html",context)

def center_update(request,id):
    try:
        object = Center.objects.get(id=id)
    except Center.DoesNotExist:
        raise Http404("Center not found.")
    if request.method == "POST":
        form = forms.CenterForm(request.POST,instance=object)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse("center:center_detail",kwargs={"id" : object.id}))
        else:
            context = {
                "form" : form
            }
            return render(request,"./center/center_update.html",context)
    context = {
        "form" : forms.CenterForm(instance = object)
    }
    return render(request,"./center/center_update.html",context)

def center_delete(request,id):
    try:
        object = Center.objects.get(id=id)
    except Center.DoesNotExist():
        raise Http404("Center data was not found.")
    if request.method == "POST":
        object.delete()
        return HttpResponseRedirect(reverse("center:center_list"))
    context = {
        "center" : object
    }
    return render(request,"./center/center_delete.html",context)
    
    

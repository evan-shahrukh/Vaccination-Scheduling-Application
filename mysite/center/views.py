from typing import Any
from django.shortcuts import render
from center.models import Center,Storage
from center import forms

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def center_list(request):
    object = Center.objects.all()
    pagination = Paginator(object,2)
    page_number = request.GET.get("page")
    page_obj = pagination.get_page(page_number)
    context = {
        "page_obj" : page_obj
    }
    return render(request,"./center/center_list.html",context)

def center_detail(request,id):
    try:
        object = Center.objects.get(id=id)
    except Center.DoesNotExist:
        raise http404("Center detail not found.")
    context = {
        "center" : object
    }
    return render(request,"./center/center_detail.html",context)

def center_create(request):
    if request.method == "POST":
        form = forms.CenterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"You have successfully created a center.")
            return HttpResponseRedirect(reverse("center:center_list"))
        else:
            context = {
                "form" : form
            }
            messages.error(request,"you have failed to create a center.")
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
            messages.success(request,"You have successfully updated a center.")
            return HttpResponseRedirect(reverse("center:center_detail",kwargs={"id" : object.id}))
        else:
            context = {
                "form" : form
            }
            messages.error(request,"you have failed to update a center")
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
        messages.success(request,"you hace successfully deleted a center.")
        return HttpResponseRedirect(reverse("center:center_list"))
    context = {
        "center" : object
    }
    return render(request,"./center/center_delete.html",context)
    
    
class StorageList(ListView):
    queryset = Storage.objects.all()
    template_name = "./storage/storage_list.html"
    ordering = ["vaccine__name"]
    paginate_by = 2
    def get_queryset(self):
        return super().get_queryset().filter(center_id=self.kwargs["id"])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["center_id"] = self.kwargs["id"]
        return context

class StorageDetail(DetailView):
    model = Storage
    template_name = "./storage/storage_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["available_quantity"] = self.object.total_quantity - self.object.booked_quantity
        return context
    
class StorageCreate(SuccessMessageMixin,CreateView):
    model = Storage
    form_class = forms.StorageForm
    template_name = "./storage/storage_create.html"
    success_message = "Storage Created Successfully!!!"
    
    def get_form_kwargs(self):
        kwargs =  super().get_form_kwargs()
        kwargs["center_id"] = self.kwargs["id"]
        return kwargs
    
    def get_initial(self):
        initial =  super().get_initial()
        initial["center"] = Center.objects.get(id=self.kwargs["id"])
        return initial
    
    def get_success_url(self):
        return reverse("center:storage_list",kwargs={"id" : self.kwargs["id"]})
    
class StorageUpdate(SuccessMessageMixin,UpdateView):
    model = Storage
    form_class = forms.StorageForm
    template_name = "./storage/storage_update.html"
    success_message = "Storage Updated Successfully!!!"
    
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs =  super().get_form_kwargs()
        kwargs["center_id"] = self.get_object().center.id
        return kwargs
    
    def get_success_url(self) -> str:
        return reverse("center:storage_list",kwargs={"id" : self.get_object().center.id})

class StorageDelete(SuccessMessageMixin,DeleteView):
    model = Storage
    template_name = "./storage/storage_delete.html"
    success_message = "Storage Deleted Successfully!!!"
    
    def get_success_url(self) -> str:
        return reverse("center:storage_list",kwargs={"id" : self.get_object().center.id})
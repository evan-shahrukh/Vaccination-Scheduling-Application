from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse

from django.views import View
from vaccine.models import Vaccine
from vaccine.forms import VaccineForm

from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required,name="dispatch")
class VaccineList(View):
    def get(self,request):
        vaccine_list = Vaccine.objects.all().order_by("name")
        pagination = Paginator(vaccine_list,2)
        page_number = request.GET.get("page")
        page_obj = pagination.get_page(page_number)
        context = {
            "page_obj" : page_obj,
        }
        return render(request,"./vaccine/vaccine_list.html",context)

@method_decorator(login_required,name="dispatch")
class VaccineDetail(View):
    def get(self,request,id):
        try:
            vaccine_detail = Vaccine.objects.get(id=id)
        except Vaccine.DoesNotExist:
            raise Http404("Vaccine detail not found.")
        context = {
            "vaccine" : vaccine_detail,
        }
        return render(request,"./vaccine/vaccine_detail.html",context)

@method_decorator(login_required,name="dispatch")
@method_decorator(permission_required("vaccine.add_vaccine",raise_exception=True),name="dispatch")
class VaccineCreate(View):
    form_name = VaccineForm
    template_name = "./vaccine/vaccine_create.html"
    def get(self,request):
        context={
            "form" : self.form_name,
        }
        return render(request,self.template_name,context)
    def post(self,request):
        form = self.form_name(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"Vaccine Created Successfully!!!")
            return HttpResponseRedirect(reverse("vaccine:vaccine_list"))
        context = {
            "form" : form
        }
        messages.error(request,"Please enter valid data!")
        return render(request,self.template_name,context)

@method_decorator(login_required,name="dispatch")
@method_decorator(permission_required("vaccine.change_vaccine",raise_exception=True),name="dispatch")
class VaccineUpdate(View):
    form_name = VaccineForm
    template_name = "./vaccine/vaccine_update.html"
    def get(self,request,id):
        vaccine = get_object_or_404(Vaccine,id=id)
        context={
            "form" : self.form_name(instance=vaccine),
        }
        return render(request,self.template_name,context)
    def post(self,request,id):
        vaccine = get_object_or_404(Vaccine,id=id)
        form = self.form_name(request.POST,instance=vaccine)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"Vaccine Updated Successfully!!!")
            return HttpResponseRedirect(reverse("vaccine:vaccine_list"))
        context={
            "form" : form,
        }
        messages.error(request,"Please enter valid data!")
        return render(request,self.template_name,context)

@method_decorator(login_required,name="dispatch")
@method_decorator(permission_required("vaccine.delete_vaccine",raise_exception=True),name="dispatch")
class VaccineDelete(View):
    template_name = "./vaccine/vaccine_delete.html"
    def get(self,request,id):
        vaccine = get_object_or_404(Vaccine,id=id)
        context = {
            "vaccine" : vaccine,
        }
        return render(request,self.template_name,context)
    def post(self,request,id):
        vaccine = get_object_or_404(Vaccine,id=id)
        vaccine.delete()
        messages.success(request,"Vaccine Deleted Successfully!!!")
        return HttpResponseRedirect(reverse("vaccine:vaccine_list"))
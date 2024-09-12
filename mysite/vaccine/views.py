from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse

from django.views import View
from vaccine.models import Vaccine
from vaccine.forms import VaccineForm

from django.shortcuts import get_object_or_404

# Create your views here.

class VaccineList(View):
    def get(self,request):
        vaccine_list = Vaccine.objects.all()
        context = {
            "vaccine" : vaccine_list,
        }
        return render(request,"./vaccine/vaccine_list.html",context)

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
            return HttpResponseRedirect(reverse("vaccine:vaccine_list"))
        context = {
            "form" : form
        }
        return render(request,self.template_name,context)

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
            return HttpResponseRedirect(reverse("vaccine:vaccine_list"))
        context={
            "form" : form,
        }
        return render(request,self.template_name,context)

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
        return HttpResponseRedirect(reverse("vaccine:vaccine_list"))
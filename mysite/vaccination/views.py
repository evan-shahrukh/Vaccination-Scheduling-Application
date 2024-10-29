from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

from vaccine.models import Vaccine
from campaign.models import Campaign,Slot
from vaccination.models import Vaccination

from django.utils import timezone
from vaccination.forms import VaccinationForm
from django.views import View
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied

from vaccination.utils import generate_pdf
from django.contrib.auth.decorators import login_required

# Create your views here.

class ChooseVaccine(LoginRequiredMixin,generic.ListView):
    model = Vaccine
    template_name = "vaccination/choose-vaccine.html"
    paginate_by = 3
    ordering = ["name"]

class ChooseCampaign(LoginRequiredMixin,generic.ListView):
    model = Campaign
    template_name = "vaccination/choose-campaign.html"
    paginate_by = 3
    ordering = ["start_date"]
    
    def get_queryset(self):
        # return super().get_queryset().filter(vaccine=self.kwargs["id"])
        queryset = Campaign.objects.filter(vaccine=self.kwargs["id"])
        return queryset

class ChooseSlot(LoginRequiredMixin,generic.ListView):
    model = Slot
    template_name = "vaccination/choose-slot.html"
    paginate_by = 3
    ordering = ["date"]
    
    def get_queryset(self):
        return super().get_queryset().filter(campaign = self.kwargs["id"],date__gte=timezone.now())

class ConfirmVaccination(View):
    form_class = VaccinationForm
    
    def get(self,request,*args,**kwargs):
        campaign = Campaign.objects.get(id=self.kwargs["campaign_id"])
        slot = Slot.objects.get(id=self.kwargs["slot_id"])
        
        form = self.form_class(initial={
            "patient" : request.user,
            "campaign" : campaign,
            "slot" : slot
        })
        
        context = {
            "patient" : request.user,
            "campaign" : campaign,
            "slot" : slot,
            "form" : form 
        }
        return render(request,"./vaccination/confirm-vaccination.html",context)
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            reserved = Slot.is_reserved(self,self.kwargs["campaign_id"],self.kwargs["slot_id"])
            if reserved:
                form.save()
                return HttpResponse("Vaccination successfully Registered!")
            return HttpResponseBadRequest("Unable to reserve vaccination at this moment!")
        return HttpResponseBadRequest("Invalid Data!")

class VaccinationList(LoginRequiredMixin,generic.ListView):
    model = Vaccination
    template_name = "vaccination/vaccination-list.html"
    paginate_by = 3
    ordering = ["campaign"]
    
    def get_queryset(self):
        return super().get_queryset().filter(patient= self.request.user)

class VaccinationDetail(LoginRequiredMixin,generic.DetailView):
    model = Vaccination
    template_name = "vaccination/vaccination-detail.html"

@login_required  
def appointment_letter(request,vaccination_id):
    vaccination = Vaccination.objects.get(id=vaccination_id)
    context={
        "pdf_title" : f"{vaccination.patient.get_full_name()} | Appointment Letter",
        "date" : str(timezone.now()),
        "title" : "Appointment Letter",
        "subtitle" : "To whom it may concern,",
        "content" : f"This is to inform you that {vaccination.campaign.vaccine.name} of Mr/Ms {vaccination.patient.get_full_name()} is scheduled on {vaccination.slot.date}."
    }
    return generate_pdf(context)

@login_required
def vaccination_certificate(request,vaccination_id):
    vaccination = Vaccination.objects.get(id=vaccination_id)
    if vaccination.is_vaccinated:
        context={
        "pdf_title" : f"Vaccination Certificate",
        "date" : str(timezone.now()),
        "title" : "Appointment Letter",
        "subtitle" : "To whom it may concern,",
        "content" : f"This is to certify that Mr/Ms {vaccination.patient.get_full_name()} has successfully taken {vaccination.campaign.vaccine.name} on {vaccination.date}. The vaccination was scheduled on {vaccination.slot.date} {vaccination.slot.start_time} at {vaccination.campaign.center.name}."
        }
        return generate_pdf(context)
    return HttpResponseBadRequest("User is not vaccinated!")

def approve_vaccination(request,vaccination_id):
    if request.user.has_perm("vaccination.change_vaccination"):
        try:
            vaccination = Vaccination.objects.get(id=vaccination_id)
        except Vaccination.DoesNotExist:
            raise PermissionDenied("vaccination with the given id doesn't exist.")
        if request.user in vaccination.campaign.agents.all():
            if vaccination.is_vaccinated:
                return HttpResponse("Patient is already vaccinated!")
            vaccination.is_vaccinated = True
            vaccination.date = timezone.now()
            vaccination.updated_by = request.user
            vaccination.save()
            return HttpResponseRedirect(reverse("vaccination:vaccination-detail",kwargs={"pk" : vaccination_id}))
        raise PermissionDenied("Invalid user!") 
    raise PermissionDenied("User doesn't have the permission!")
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Campaign,Slot
from vaccination.models import Vaccination
from .forms import CampaignForm,SlotForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy,reverse

# Create your views here.

class CampaignList(LoginRequiredMixin,ListView):
    model = Campaign
    template_name="./campaign/campaign-list.html"
    paginate_by = "10"
    ordering = ["-id"]
    
class CampaignDetail(LoginRequiredMixin,DetailView):
    model = Campaign
    template_name = "./campaign/campaign-detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["registration"] = Vaccination.objects.filter(campaign=self.kwargs["pk"]).count()
        return context

class CampaignCreate(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Campaign
    form_class = CampaignForm
    template_name = "./campaign/campaign-create.html"
    permission_required =("campaign.add_campaign",)
    success_message = "Campaign created successfully !!!"
    success_url = reverse_lazy("campaign:campaign-create")

class CampaignUpdate(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Campaign
    form_class = CampaignForm
    template_name = "./campaign/campaign-update.html"
    permission_required =("campaign.change_campaign",)
    success_message = "Campaign updated successfully !!!"
    
    def get_success_url(self) -> str:
        return reverse("campaign:campaign-detail",kwargs={'pk' : self.kwargs["pk"]})

class CampaignDelete(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Campaign
    template_name = "./campaign/campaign-delete.html"
    permission_required =("campaign.delete_campaign",)
    success_message = "Campaign Deleted successfully !!!"
    success_url = reverse_lazy("campaign:campaign-list")

class SlotList(LoginRequiredMixin,ListView):
    model = Slot
    template_name = "./slot/slot-list.html"
    paginate_by = 5
    
    def get_queryset(self):
        queryset = Slot.objects.filter(campaign=self.kwargs["id"]).order_by("id")
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["campaign_id"] = self.kwargs["id"]
        return context

class SlotDetail(LoginRequiredMixin,DetailView):
    model = Slot
    template_name = "./slot/slot-detail.html"
    
class SlotCreate(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Slot
    form_class = SlotForm
    template_name = "./slot/slot-create.html"
    permission_required = ("campaign.add_slot",)
    success_message = "Slot created successfully !!!"
    
    def get_success_url(self) -> str:
        return reverse("campaign:slot-list",kwargs={"kwargs" : self.kwargs["campaign_id"]})
    
    def get_initial(self):
        initial = super().get_initial()
        initial["campaign"] = Campaign.objects.get(id=self.kwargs["campaign_id"])
        return initial
    
    def get_form_kwargs(self):
        kwargs =  super().get_form_kwargs()
        kwargs["campaign_id"] = self.kwargs["campaign_id"]
        return kwargs

class SlotUpdate(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Slot
    form_class = SlotForm
    template_name = "./slot/slot-update.html"
    permission_required = ("campaign.change_slot",)
    success_message = "Slot updated successfully !!!"
    
    def get_success_url(self):
        return reverse_lazy("campaign:slot-detail",kwargs={"pk" : self.kwargs["pk"]})

    
    
    def get_form_kwargs(self):
        kwargs =  super().get_form_kwargs()
        kwargs["campaign_id"] = self.get_object().campaign.id
        return kwargs

class SlotDelete(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Slot
    template_name = "./slot/slot-delete.html"
    permission_required = ("campaign.delete_slot",)
    success_message = "Slot deleted successfully !!!"
    
    def get_success_url(self):
        return reverse_lazy("campaign:slot-list",kwargs={"id" : self.get_object().campaign.id})
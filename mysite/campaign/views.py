from django.shortcuts import render
from .models import Campaign
from vaccination.models import Vaccination
from .forms import CampaignForm
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
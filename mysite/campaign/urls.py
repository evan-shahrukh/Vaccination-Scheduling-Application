from django.urls import path
from campaign.views import CampaignList,CampaignDetail,CampaignCreate,CampaignUpdate,CampaignDelete

app_name = "campaign"

urlpatterns = [
    path("",CampaignList.as_view(),name="campaign-list"),
    path("<int:pk>/",CampaignDetail.as_view(),name="campaign-detail"),
    path("create/",CampaignCreate.as_view(),name="campaign-create"),
    path("update/<int:pk>",CampaignUpdate.as_view(),name="campaign-update"),
    path("delete/<int:pk>",CampaignDelete.as_view(),name="campaign-delete"),
]

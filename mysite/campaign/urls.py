from django.urls import path
from campaign.views import CampaignList,CampaignDetail,CampaignCreate,CampaignUpdate,CampaignDelete,SlotList,SlotDetail,SlotCreate,SlotUpdate,SlotDelete

app_name = "campaign"

urlpatterns = [
    path("",CampaignList.as_view(),name="campaign-list"),
    path("<int:pk>/",CampaignDetail.as_view(),name="campaign-detail"),
    path("create/",CampaignCreate.as_view(),name="campaign-create"),
    path("update/<int:pk>",CampaignUpdate.as_view(),name="campaign-update"),
    path("delete/<int:pk>",CampaignDelete.as_view(),name="campaign-delete"),
    path("<int:id>/slot/",SlotList.as_view(),name="slot-list"),
    path("slot/<int:pk>/",SlotDetail.as_view(),name="slot-detail"),
    path("<int:campaign_id>/slot/create/",SlotCreate.as_view(),name="slot-create"),
    path("slot/update/<int:pk>/",SlotUpdate.as_view(),name="slot-update"),
    path("slot/delete/<int:pk>/",SlotDelete.as_view(),name="slot-delete"),
]

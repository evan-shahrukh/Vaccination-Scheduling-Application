from django.urls import path
from vaccination.views import ChooseVaccine,ChooseCampaign,ChooseSlot,ConfirmVaccination,VaccinationList,VaccinationDetail,appointment_letter,vaccination_certificate

app_name = "vaccination"

urlpatterns = [
    path("",VaccinationList.as_view(),name="vaccination-list"),
    path("detail/<int:pk>",VaccinationDetail.as_view(),name="vaccination-detail"),
    path("vaccine/",ChooseVaccine.as_view(),name="choose-vaccine"),
    path("campaign/<int:id>/",ChooseCampaign.as_view(),name="choose-campaign"),
    path("campaign/slot/<int:id>/",ChooseSlot.as_view(),name="choose-slot"),
    path("confirm_vaccination/<int:campaign_id>/<int:slot_id>/",ConfirmVaccination.as_view(),name="confirm-vaccination"),
    path("appointment_letter/<int:vaccination_id>",appointment_letter,name="appointment-letter"),
    path("vaccination_certificate/<int:vaccination_id>",vaccination_certificate,name="vaccination-certificate"),
]

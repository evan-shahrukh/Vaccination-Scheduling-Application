from django.urls import path
from vaccine.views import VaccineList,VaccineDetail,VaccineCreate,VaccineUpdate,VaccineDelete

app_name = "vaccine"

urlpatterns = [
    path("",VaccineList.as_view(),name="vaccine_list"),
    path("<int:id>/",VaccineDetail.as_view(),name="vaccine_detail"),
    path("create/",VaccineCreate.as_view(),name="vaccine_create"),
    path("update/<int:id>/",VaccineUpdate.as_view(),name="vaccine_update"),
    path("delete/<int:id>/",VaccineDelete.as_view(),name="vaccine_delete"),
]

from django.urls import path
from center import views 

app_name = "center"

urlpatterns = [
    path("",views.center_list,name="center_list"),
    path("<int:id>/",views.center_detail,name="center_detail"),
    path("create/",views.center_create,name="center_create"),
    path("update/<int:id>/",views.center_update,name="center_update"),
    path("delete/<int:id>/",views.center_delete,name="center_delete"),
]

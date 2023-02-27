from django.urls import path

from api.views import VistaCVE, Vistasumarizada

#define routes  for the api
urlpatterns=[
    path("",VistaCVE.as_view(),name="lista_vulnerabilidades"),
    path("sumarizada",Vistasumarizada.as_view(),name="informacion_sumarizada")
]
from django.urls import path
from . import views


urlpatterns = [
    path("mapping/",views.mapping, name="mapping"),
    path("mappoint/",views.pointing, name="mappoint"),
    path("bokji/", views.bokji, name="bokji"),
    path("boho/", views.boho, name="boho"),
]
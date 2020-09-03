from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import Seouldata, Datasample, Sample
import csv
import math

def mapping(request):
    maplist = Seouldata.objects.all()
    context = {"maplist": maplist}
    return render(request, "map.html",context)

def pointing(request):
    pin_lat=[]
    pin_lng=[]
    pin_name = []
    pin_addr = []
    pin_tel = []
    pin_kind = []
    pin_kind_detail = []
    points = Sample.objects.all()
    for data in points:
        pin_lat.append(data.lat)
        pin_lng.append(data.lng)
        pin_name.append(data.name)
        pin_addr.append(data.addr)
        pin_tel.append(data.tel)
        pin_kind.append(data.kind)
        pin_kind_detail.append(data.kind_detail)
    pin = {"pin_lat": pin_lat, "pin_lng": pin_lng,
           "pin_name":pin_name, "pin_addr": pin_addr,
           "pin_tel": pin_tel, "pin_kind": pin_kind,
           "pin_kind_detail": pin_kind_detail}
    return JsonResponse(pin, json_dumps_params={'ensure_ascii':False})


def bokji(request):
    bokji_name = []
    bokji_addr = []
    bokji_tel = []
    bokji_lat = []
    bokji_lng = []
    list = Sample.objects.filter(kind="복지시설")
    for data in list:
        bokji_name.append(data.name)
        bokji_addr.append(data.addr)
        bokji_tel.append(data.tel)
        bokji_lat.append(data.lat)
        bokji_lng.append(data.lng)
    bokji = {"bokji_name": bokji_name, "bokji_addr": bokji_addr, "bokji_tel": bokji_tel,
             "bokji_lat": bokji_lat, "bokji_lng": bokji_lng }
    return JsonResponse(bokji, json_dumps_params={'ensure_ascii':False})

def boho(request):
    boho_name = []
    boho_addr = []
    boho_tel = []
    boho_lat = []
    boho_lng = []
    list = Sample.objects.filter(kind="보호시설")
    for data in list:
        boho_name.append(data.name)
        boho_addr.append(data.addr)
        boho_tel.append(data.tel)
        boho_lat.append(data.lat)
        boho_lng.append(data.lng)
    bokji = {"boho_name": boho_name, "boho_addr": boho_addr, "boho_tel": boho_tel,
             "boho_lat": boho_lat, "boho_lng": boho_lng }
    return JsonResponse(bokji, json_dumps_params={'ensure_ascii':False})

# Create your views here.

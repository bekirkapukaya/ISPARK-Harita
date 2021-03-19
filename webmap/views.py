from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

from django.views.decorators.csrf import csrf_exempt
from .models import Ispark
import requests

IBB_API = "https://data.ibb.gov.tr/api/3/action/datastore_search?resource_id=c3eb0d72-1ce4-4983-a3a8-6b0b4b19fcb9"


@csrf_exempt
def updateDatabase(request):
    rawData = requests.get(IBB_API)
    jsonData = rawData.json()
    duraklar = jsonData["result"]["records"]
    for durak in duraklar:
        if durak["Enlem/Boylam"] != "":
            guncelDuraklar = Ispark(
                parkId=durak["Park ID"],
                parkName=durak["Park Adi"],
                locationId=durak["Lokasyon ID"],
                locationCode=durak["Lokasyon Kodu"],
                locationName=durak["Lokasyon Adi"],
                parkTypeId=durak["Park Tipi ID"],
                parkType=durak["Park Tipi"],
                parkCapacity=durak["Park Kapasitesi"],
                workHours=durak["Calisma Saatleri"],
                regionId=durak["Bolge ID"],
                region=durak["Bolge"],
                subRegionId=durak["Alt Bolge ID"],
                subRegion=durak["Alt Bolge"],
                boroughld=durak["Ilce ID"],
                borough=durak["Ilce"],
                address=durak["Adres"],
                point=durak["Enlem/Boylam"],
                polygon=durak["Polygon Verisi"],
                lat=durak["Boylam"],
                lon=durak["Enlem"],
                monthlyPrice=durak["Aylik Abonelik Ucreti"],
                freeParkingTime=durak["Ucretsiz Parklanma Suresi (dakika)"],
                price=durak["Tarifesi"],
                parkAndGoPoint=durak["Park Et Devam Et Noktasi"],
                geom=durak["Enlem/Boylam"])
            guncelDuraklar.save()

    return redirect("/map")


def mapPage(request):
    return render(request, "map.html")


@csrf_exempt
def getPoints(request):
    points = Ispark.objects.all()
    data = serialize("geojson", points, geometry_field='geom', srid=4326)
    return HttpResponse(data)

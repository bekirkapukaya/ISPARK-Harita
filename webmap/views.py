from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from .models import Ispark
import requests

IBB_API = "https://data.ibb.gov.tr/api/3/action/datastore_search?resource_id=c3eb0d72-1ce4-4983-a3a8-6b0b4b19fcb9"

@login_required(login_url="user:login")
def mapPage(request):
    return render(request, "map.html")

@login_required(login_url="user:login")
def editLocationPage(request, id):
    gecerliDurak = Ispark.objects.filter(parkId=id)
    durakBilgileri = list(gecerliDurak)
    context = {
        "parkId": durakBilgileri[0].parkId,
        "parkName": durakBilgileri[0].parkName,
        "locationId": durakBilgileri[0].locationId,
        "locationCode": durakBilgileri[0].locationCode,
        "locationName": durakBilgileri[0].locationName,
        "parkTypeId": durakBilgileri[0].parkTypeId,
        "parkType": durakBilgileri[0].parkType,
        "parkCapacity": durakBilgileri[0].parkCapacity,
        "workHours": durakBilgileri[0].workHours,
        "regionId": durakBilgileri[0].regionId,
        "region": durakBilgileri[0].region,
        "subRegionId": durakBilgileri[0].subRegionId,
        "subRegion": durakBilgileri[0].subRegion,
        "boroughld": durakBilgileri[0].boroughld,
        "borough": durakBilgileri[0].borough,
        "address": durakBilgileri[0].address,
        "monthlyPrice": durakBilgileri[0].monthlyPrice,
        "freeParkingTime": durakBilgileri[0].freeParkingTime,
        "price": durakBilgileri[0].price,
        "parkAndGoPoint": durakBilgileri[0].parkAndGoPoint,
    }

    return render(request, "editlocation.html", context)


@csrf_exempt
def updateDatabase(request):
    rawData = requests.get(IBB_API)
    jsonData = rawData.json()
    apiDuraklar = jsonData["result"]["records"]
    dbDuraklar = Ispark.objects.values()
    print(len(dbDuraklar))
    if len(dbDuraklar) != 0:
        for apiDurak in apiDuraklar:
            for dbDurak in dbDuraklar:
                if apiDurak["Enlem/Boylam"] == dbDurak["point"] and apiDurak["Enlem/Boylam"] != "":
                    print(apiDurak["Park Adi"])
                    """
                    guncelDuraklar = Ispark(
                        parkId=apiDurak["Park ID"],
                        parkName=apiDurak["Park Adi"],
                        locationId=apiDurak["Lokasyon ID"],
                        locationCode=apiDurak["Lokasyon Kodu"],
                        locationName=apiDurak["Lokasyon Adi"],
                        parkTypeId=apiDurak["Park Tipi ID"],
                        parkType=apiDurak["Park Tipi"],
                        parkCapacity=apiDurak["Park Kapasitesi"],
                        workHours=apiDurak["Calisma Saatleri"],
                        regionId=apiDurak["Bolge ID"],
                        region=apiDurak["Bolge"],
                        subRegionId=apiDurak["Alt Bolge ID"],
                        subRegion=apiDurak["Alt Bolge"],
                        boroughld=apiDurak["Ilce ID"],
                        borough=apiDurak["Ilce"],
                        address=apiDurak["Adres"],
                        point=apiDurak["Enlem/Boylam"],
                        polygon=apiDurak["Polygon Verisi"],
                        lat=apiDurak["Boylam"],
                        lon=apiDurak["Enlem"],
                        monthlyPrice=apiDurak["Aylik Abonelik Ucreti"],
                        freeParkingTime=apiDurak["Ucretsiz Parklanma Suresi (dakika)"],
                        price=apiDurak["Tarifesi"],
                        parkAndGoPoint=apiDurak["Park Et Devam Et Noktasi"],
                        geom=apiDurak["Enlem/Boylam"])
                    guncelDuraklar.save()
                    """
    else:
        for apiDurak in apiDuraklar:
            if apiDurak["Enlem/Boylam"] != "":
                guncelDuraklar = Ispark(
                    parkId=apiDurak["Park ID"],
                    parkName=apiDurak["Park Adi"],
                    locationId=apiDurak["Lokasyon ID"],
                    locationCode=apiDurak["Lokasyon Kodu"],
                    locationName=apiDurak["Lokasyon Adi"],
                    parkTypeId=apiDurak["Park Tipi ID"],
                    parkType=apiDurak["Park Tipi"],
                    parkCapacity=apiDurak["Park Kapasitesi"],
                    workHours=apiDurak["Calisma Saatleri"],
                    regionId=apiDurak["Bolge ID"],
                    region=apiDurak["Bolge"],
                    subRegionId=apiDurak["Alt Bolge ID"],
                    subRegion=apiDurak["Alt Bolge"],
                    boroughld=apiDurak["Ilce ID"],
                    borough=apiDurak["Ilce"],
                    address=apiDurak["Adres"],
                    point=apiDurak["Enlem/Boylam"],
                    polygon=apiDurak["Polygon Verisi"],
                    lat=apiDurak["Boylam"],
                    lon=apiDurak["Enlem"],
                    monthlyPrice=apiDurak["Aylik Abonelik Ucreti"],
                    freeParkingTime=apiDurak["Ucretsiz Parklanma Suresi (dakika)"],
                    price=apiDurak["Tarifesi"],
                    parkAndGoPoint=apiDurak["Park Et Devam Et Noktasi"],
                    geom=apiDurak["Enlem/Boylam"])
                guncelDuraklar.save()

    return redirect("/map")


@csrf_exempt
def getPoints(request):
    points = Ispark.objects.all()
    data = serialize("geojson", points, geometry_field='geom', srid=4326)
    return HttpResponse(data)


@csrf_exempt
def updatePoint(request, id):
    pass


@csrf_exempt
def deletePoint(request, id):
    print(id)

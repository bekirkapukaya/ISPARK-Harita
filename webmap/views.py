from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import IsparkForm

from .models import Ispark
import pandas

#IBB_API = "https://data.ibb.gov.tr/api/3/action/datastore_search?resource_id=c3eb0d72-1ce4-4983-a3a8-6b0b4b19fcb9"
IBB_EXCEL = "https://data.ibb.gov.tr/dataset/913dbba2-192f-404c-995b-1b880a7d7609/resource/c3eb0d72-1ce4-4983-a3a8-6b0b4b19fcb9/download/ispark-otoparklarna-ait-bilgiler.xlsx"


@login_required(login_url="user:login")
def mapPage(request):
    return render(request, "map.html")


@login_required(login_url="user:login")
def editLocationPage(request, id):
    durak = get_object_or_404(Ispark, parkId=id)
    form = IsparkForm(request.POST or None, instance=durak)

    if form.is_valid():
        durak = form.save()
        durak.save()

        messages.success(request, "Durak başarıyla güncellendi...")
        return redirect("webmap:map")

    return render(request, "editlocation.html", {"form": form})


@login_required(login_url="user:login")
def updateDatabase(request):
    duraklar = pandas.read_excel(
        IBB_EXCEL,
        engine='openpyxl',
        sheet_name=2,
        usecols=['Park ID', 'Park Adı', 'Lokasyon ID', 'Lokasyon Kodu', 'Lokasyon Adı', 'Park Tipi ID',
                 'Park Tipi', 'Park Kapasitesi', 'Calışma Saatleri', 'Bölge ID', 'Bölge', 'Alt Bölge ID', 'Alt Bölge',
                 'İlçe ID', 'İlçe', 'Adres', 'Enlem/Boylam', 'Polygon Verisi', 'Boylam', 'Enlem', 'Aylık Abonelik Ücreti',
                 'Ücretsiz Parklanma Süresi (dakika)', 'Tarifesi', 'Park Et Devam Et Noktası', ])
    filterDuraklar = duraklar.dropna(subset=['Enlem/Boylam'])

    apiDuraklar = filterDuraklar.to_dict(orient='records')
    dbDuraklar = Ispark.objects.values()

    apiKayitli = []
    dbKayitli = []
    fark = []
    for apiDurak in apiDuraklar:
        apiKayitli.append(apiDurak["Park ID"])
        for dbDurak in dbDuraklar:
            if apiDurak["Park ID"] == dbDurak["parkId"]:
                dbKayitli.append(apiDurak["Park ID"])

    def Diff(li1, li2):
        return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

    guncelDuraklar = Diff(apiKayitli, dbKayitli)
    countGuncelDurak = len(guncelDuraklar)

    for apiDurak in apiDuraklar:
        for durak in guncelDuraklar:
            if apiDurak["Park ID"] == durak:
                yeniDuraklar = Ispark(
                    parkId=apiDurak["Park ID"],
                    parkName=apiDurak["Park Adı"],
                    locationId=apiDurak["Lokasyon ID"],
                    locationCode=apiDurak["Lokasyon Kodu"],
                    locationName=apiDurak["Lokasyon Adı"],
                    parkTypeId=apiDurak["Park Tipi ID"],
                    parkType=apiDurak["Park Tipi"],
                    parkCapacity=apiDurak["Park Kapasitesi"],
                    workHours=apiDurak["Calışma Saatleri"],
                    regionId=apiDurak["Bölge ID"],
                    region=apiDurak["Bölge"],
                    subRegionId=apiDurak["Alt Bölge ID"],
                    subRegion=apiDurak["Alt Bölge"],
                    boroughld=apiDurak["İlçe ID"],
                    borough=apiDurak["İlçe"],
                    address=apiDurak["Adres"],
                    point=apiDurak["Enlem/Boylam"],
                    polygon=apiDurak["Polygon Verisi"],
                    lat=apiDurak["Boylam"],
                    lon=apiDurak["Enlem"],
                    monthlyPrice=apiDurak["Aylık Abonelik Ücreti"],
                    freeParkingTime=apiDurak["Ücretsiz Parklanma Süresi (dakika)"],
                    price=apiDurak["Tarifesi"],
                    parkAndGoPoint=apiDurak["Park Et Devam Et Noktası"],
                    geom=apiDurak["Enlem/Boylam"])
                yeniDuraklar.save()
    messages.success(
        request, "İBB sunucusundan {} adet yeni durak veritabanına kayıt edildi...".format(countGuncelDurak))

    """
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
    else:
        sayac = 0
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
                sayac +=1
        messages.success(request, "İBB sunucusundan {} adet durak veritabanına kayıt edildi...".format(sayac))
    """
    return redirect("webmap:map")


@login_required(login_url="user:login")
def getPoints(request):
    points = Ispark.objects.all()
    data = serialize("geojson", points, geometry_field='geom', srid=4326)
    return HttpResponse(data)


@login_required(login_url="user:login")
def deletePoint(request, id):
    location = get_object_or_404(Ispark, parkId=id)
    location.delete()
    messages.success(request, "Durak başarıyla silindi...")
    return redirect("webmap:map")

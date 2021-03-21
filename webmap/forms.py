from django import forms
from .models import Ispark


class IsparkForm(forms.ModelForm):
    class Meta:
        model = Ispark
        fields = ["parkName", "locationId", "locationCode", "locationName", "parkTypeId", "parkType", "parkCapacity", "workHours",
                  "regionId", "region", "subRegionId", "subRegion", "boroughld", "borough", "address", "monthlyPrice", "freeParkingTime", "price", "parkAndGoPoint"]

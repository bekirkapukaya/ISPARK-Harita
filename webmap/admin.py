from django.contrib import admin
from .models import Ispark


@admin.register(Ispark)
class IsparkAdmin(admin.ModelAdmin):
    list_display = ["parkName", "parkType", "borough",
                    "parkCapacity", "monthlyPrice", "workHours"]
    search_fields = ["parkName"]
    list_filter = ["borough"]

    class Meta:
        model = Ispark

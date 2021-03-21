from django.contrib import admin
from django.urls import path
from . import views
app_name = "webmap"

urlpatterns = [
    path('', views.mapPage, name="map"),
    path('editlocation/<int:id>', views.editLocationPage, name="editLocation"),
    path('updatedb', views.updateDatabase),
    path('getpoints', views.getPoints),
    path('updatepoint/<int:id>', views.updatePoint),
    path('deletepoint/<int:id>', views.deletePoint)
]
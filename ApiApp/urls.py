from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'ApiApp'

urlpatterns = [
    path('jadwals/',views.readjadwal),
    path('jadwal/<int:id>',views.detailjadwal),
    path('create/',views.createjadwal),
    path('edit/<int:id>',views.updatejadwal),
    path('hapus/<int:id>',views.deletejadwal),
]

from django.urls import path
from beli_paket.views import show_beli_paket

app_name = 'beli_paket'

urlpatterns = [
    path('/beli-paket', show_beli_paket, name='beli_paket'),
]
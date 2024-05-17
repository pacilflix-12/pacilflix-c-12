from django.urls import path
from langganan.views import langganan_view
from beli_paket.views import beli_paket

urlpatterns = [
    path('langganan/', langganan_view, name='langganan_view'),
    path('beli_paket/', beli_paket, name='beli_paket'),
]
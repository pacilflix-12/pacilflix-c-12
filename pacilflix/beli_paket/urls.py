from django.urls import path
from beli_paket.views import buy_package

app_name = 'beli_paket'

urlpatterns = [
    path('/buy-package', buy_package, name='buy_package'),
]
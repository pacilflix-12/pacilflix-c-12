from django.urls import path
<<<<<<< Updated upstream
from beli_paket.views import buy_package
=======
from beli_paket.views import show_beli_paket
>>>>>>> Stashed changes

app_name = 'beli_paket'

urlpatterns = [
<<<<<<< Updated upstream
    path('/buy-package', buy_package, name='buy_package'),
=======
    path('/beli-paket', show_beli_paket, name='beli_paket'),
>>>>>>> Stashed changes
]
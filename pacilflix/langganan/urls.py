from django.urls import path
from langganan.views import subscribe_list

app_name = 'daftar_kontributor'

urlpatterns = [
    path('/subscribe', subscribe_list, name='subscribe_list'),
]
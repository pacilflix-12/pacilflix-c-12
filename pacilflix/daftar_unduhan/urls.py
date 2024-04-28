from django.urls import path
from daftar_unduhan.views import download_list

app_name = 'daftar_unduhan'

urlpatterns = [
    path('', download_list, name='download_list'),
]
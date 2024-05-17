from django.urls import path
from konstributor.views import contributor_list

app_name = 'daftar_kontributor'

urlpatterns = [
    path('/contributor', contributor_list, name='contributor_list'),
]
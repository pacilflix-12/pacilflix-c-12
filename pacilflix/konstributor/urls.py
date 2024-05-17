from django.urls import path
from konstributor.views import show_kontributor

app_name = 'daftar_kontributor'

urlpatterns = [
    path('/contributor', show_kontributor, name='show_contributor'),
]

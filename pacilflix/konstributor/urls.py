from django.urls import path
from konstributor.views import show_all_contributors_with_details

app_name = 'konstributor'

urlpatterns = [
    path('contributors/', show_all_contributors_with_details, name='all_contributors_with_details')
]

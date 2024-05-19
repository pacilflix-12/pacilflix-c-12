from django.urls import path
from .views import manage_subscription, buy_package, purchase_package_view

app_name = 'langganan'

urlpatterns = [
    path('', manage_subscription, name='manage_subscription'),
    path('buy/', buy_package, name='buy_package'),
    path('purchase/', purchase_package_view, name='purchase_package'),
]
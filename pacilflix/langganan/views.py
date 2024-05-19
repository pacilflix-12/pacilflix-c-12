from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .services import get_active_subscription, get_available_packages, get_transaction_history, purchase_package
from utils.get_user import get_user

def manage_subscription(request: HttpRequest) -> HttpResponse:
    user = request.user.username
    active_subscription = get_active_subscription(user)
    available_packages = get_available_packages()
    transaction_history = get_transaction_history(user)

    context = {
        "active_subscription": active_subscription,
        "available_packages": available_packages,
        "transaction_history": transaction_history,
        "islogin": get_user(request=request) != None
    }

    return render(request, 'langganan.html', context)

def buy_package(request: HttpRequest) -> HttpResponse:
    package_name = request.GET.get('package')
    if package_name:
        packages = get_available_packages()
        package = next((p for p in packages if p['nama'] == package_name), None)
        if package:
            context = {
                "nama": package["nama"],
                "harga": package["harga"],
                "resolusi_layar": package["resolusi_layar"],
                "dukungan_perangkat": package["dukungan_perangkat"],
                "islogin": get_user(request=request) != None
            }
            return render(request, 'beli_paket.html', context)
    return redirect('langganan:manage_subscription')

def purchase_package_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        user = request.user.username
        package_name = request.POST.get('nama')
        payment_method = request.POST.get('metode_pembayaran')
        if user and package_name and payment_method:
            purchase_package(user, package_name, payment_method)
            return redirect('langganan:manage_subscription')
    return redirect('langganan:manage_subscription')
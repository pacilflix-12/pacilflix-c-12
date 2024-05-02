from django.shortcuts import render

context = [
    {'id': 1, 'nama': 'placeholder', 'harga' : 'placeholder', 'resolusi layar': 'placeholder', 'dukungan perangkat': 'placeholder'},
    {'id': 2, 'nama': 'placeholder', 'harga' : 'placeholder', 'resolusi layar': 'placeholder', 'dukungan perangkat': 'placeholder'}
]

def buy_package(request):
    return render(request, 'beli_paket.html', {'context': context})

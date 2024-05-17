from django.shortcuts import render


context = [
    {'id': 1, 'nama': 'placeholder', 'harga' : 'placeholder', 'resolusi layar': 'placeholder', 'dukungan perangkat': 'placeholder', 
     'tanggal dimulai': 'placeholder', 'tanggal akhir': 'placeholder'},
    {'id': 2, 'nama': 'placeholder', 'harga' : 'placeholder', 'resolusi layar': 'placeholder', 'dukungan perangkat': 'placeholder', 
     'tanggal dimulai': 'placeholder', 'tanggal akhir': 'placeholder'}
]

def subscribe_list(request):
    return render(request, 'langganan.html', {'context': context})

from django.shortcuts import render



downloads = [
    {'id': 1, 'title': 'Avengers', 'waktu_unduh' : '2024-04-11 23:46:22'},
    {'id': 2, 'title': 'Harry Potter', 'waktu_unduh' : '2024-01-31 10:35:04'}
]

def download_list(request):
    return render(request, 'daftar_unduhan.html', {'downloads': downloads})

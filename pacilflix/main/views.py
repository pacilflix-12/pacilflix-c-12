from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Kelompok',
        'class': 'Basdat F'
    }

    return render(request, "tayangan_dummy.html", context)
from django.shortcuts import render


context = [
    {'id': 1, 'nama': 'placeholder', 'jenis kelamin' : 'placeholder', 'kewarganegaraan': 'placeholder'},
    {'id': 2, 'nama': 'placeholder', 'jenis kelamin' : 'placeholder', 'kewarganegaraan': 'placeholder'}
]

def contributor_list(request):
    return render(request, 'konstributor.html', {'context': context})

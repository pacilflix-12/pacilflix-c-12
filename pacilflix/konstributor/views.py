from django.db import connection
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from utils.get_user import get_user
from django.contrib.auth.decorators import login_required


@login_required(login_url='/authentication/login/')
def show_kontributor(request: HttpRequest) -> HttpResponse:
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, nama, jenis_kelamin, kewarganegaraan FROM contributors")
        rows = cursor.fetchall()
        contributors = [
            {
                'id': row[0],
                'nama': row[1],
                'jenis_kelamin': row[2],
                'kewarganegaraan': row[3],
            }
            for row in rows
        ]
    return contributors

@login_required(login_url='/authentication/login/')
def contributor_list(request):
    contributors = show_kontributor()
    return render(request, 'contributor_list.html', {'contributors': contributors})

# def filter_kontributor(request):
#     selected_option = request.GET.get('selected_option')
#     filtered_data = YourModel.objects.filter(some_field=selected_option)
#     return JsonResponse({'filtered_data': filtered_data})
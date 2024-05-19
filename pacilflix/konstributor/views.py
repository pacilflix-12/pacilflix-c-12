from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from konstributor.services import (
    get_all_contributors, 
    get_contributor_detail, 
    get_all_contributors_with_details
)
from utils.get_user import get_user


def show_all_contributors(request: HttpRequest) -> HttpResponse:
    contributors = get_all_contributors()
    context = {
        "contributors": contributors,
        "islogin": get_user(request=request) != None
    }
    return render(request, "konstributor.html", context=context)


def show_all_contributors(request: HttpRequest) -> HttpResponse:
    contributors = get_all_contributors()
    context = {
        "view_type": "all_contributors",
        "contributors": contributors,
        "islogin": get_user(request=request) != None
    }
    return render(request, "konstributor.html", context=context)


def show_contributor_detail(request: HttpRequest, id_contributor: str) -> HttpResponse:
    contributor_detail = get_contributor_detail(id_contributor)
    context = {
        "view_type": "contributor_detail",
        "contributor": contributor_detail,
        "islogin": get_user(request=request) != None
    }
    return render(request, "konstributor.html", context=context)


def show_all_contributors_with_details(request: HttpRequest) -> HttpResponse:
    contributors_with_details = get_all_contributors_with_details()
    context = {
        "view_type": "all_contributors_with_details",
        "contributors_with_details": contributors_with_details,
        "islogin": get_user(request=request) != None
    }
    return render(request, "konstributor.html", context=context)















# revisi kedua
# from django.db import connection
# from django.http import HttpResponse, HttpRequest
# from django.shortcuts import redirect, render
# from utils.get_user import get_user
# from django.contrib.auth.decorators import login_required


# @login_required(login_url='/authentication/login/')

# def show_kontributor(request):
#     if get_user(request=request) == None:
#         return redirect('/login/')
    
#     # Mengambil data kontributor dari database
#     tipe = request.GET.get('tipe', None)
    
#     # Mengambil data kontributor dari database
#     query = """
#         SELECT k.nama, p.tipe, k.jenis_kelamin, k.kewarganegaraan
#         FROM kontributor k
#         LEFT JOIN peran_kontributor p ON k.id = p.kontributor_id
#     """
#     params = []

#     if tipe:
#         query += " WHERE p.tipe = %s"
#         params.append(tipe)
    
#     with connection.cursor() as cursor:
#         cursor.execute(query, params)
#         kontributor_list = cursor.fetchall()

#     context = {
#         'kontributor_list': kontributor_list,
#         'tipe': tipe,
#     }

#     return render(request, 'konstributor.html', context)


# do i even need this let's be fr
# def filter_kontributor(request):
#     selected_option = request.GET.get('selected_option')
#     filtered_data = YourModel.objects.filter(some_field=selected_option)
#     return JsonResponse({'filtered_data': filtered_data})

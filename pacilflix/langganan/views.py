# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection

@login_required
def show_langganan(request):
    user_id = request.user.id

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                p.nama, p.harga, p.resolusi_layar, p.dukungan_perangkat, t.start_date_time, t.end_date_time
            FROM transaksi t
            JOIN paket_langganan p ON t.paket_id = p.id
            WHERE t.user_id = %s AND t.end_date_time > NOW()
            ORDER BY t.end_date_time DESC
            LIMIT 1
        """, [user_id])
        active_subscription = cursor.fetchone()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, nama, harga, resolusi_layar, dukungan_perangkat 
            FROM paket_langganan
        """)
        available_packages = cursor.fetchall()

    context = {
        'active_subscription': active_subscription,
        'available_packages': available_packages,
    }

    return render(request, 'langganan.html', context)
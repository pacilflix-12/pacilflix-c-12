<<<<<<< Updated upstream
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.utils import timezone


@login_required
def langganan_view(request):
    user = request.user

    # Mengambil informasi langganan aktif
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT nama_paket, harga, resolusi_layar, dukungan_perangkat, start_date_time, end_date_time
            FROM transaksi_langganan
            WHERE username = %s
            ORDER BY end_date_time DESC
            LIMIT 1
        """, [user.username])
        langganan_aktif = cursor.fetchone()

    # Mengambil paket yang tersedia
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, nama_paket, harga, resolusi_layar, dukungan_perangkat
            FROM paket_langganan
        """)
        paket_tersedia = cursor.fetchall()

    # Mengambil riwayat transaksi
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT nama_paket, start_date_time, end_date_time, metode_pembayaran, timestamp_pembayaran, harga
            FROM transaksi_langganan
            WHERE username = %s
            ORDER BY timestamp_pembayaran DESC
        """, [user.username])
        riwayat_transaksi = cursor.fetchall()

    context = {
        'langganan_aktif': langganan_aktif,
        'paket_tersedia': paket_tersedia,
        'riwayat_transaksi': riwayat_transaksi,
    }

    return render(request, 'langganan.html', context)
=======
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
>>>>>>> Stashed changes

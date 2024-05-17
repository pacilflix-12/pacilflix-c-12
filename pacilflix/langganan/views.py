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

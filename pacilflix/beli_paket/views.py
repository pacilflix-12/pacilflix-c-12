from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.utils import timezone

@login_required
def beli_paket(request):
    if request.method == "POST":
        paket_id = request.POST.get('paket_id')
        user = request.user

        # Mengambil detail paket
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT nama_paket, harga
                FROM paket_langganan
                WHERE id = %s
            """, [paket_id])
            paket = cursor.fetchone()

        if paket:
            nama_paket, harga = paket
            start_date_time = timezone.now()
            end_date_time = start_date_time + timezone.timedelta(days=30)

            # Memasukkan transaksi baru
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO transaksi_langganan (username, start_date_time, end_date_time, nama_paket, metode_pembayaran, timestamp_pembayaran, harga)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, [
                    user.username,
                    start_date_time,
                    end_date_time,
                    nama_paket,
                    'transfer',  # Misal metode pembayaran transfer
                    timezone.now(),
                    harga
                ])

        return redirect('langganan_view')

    return redirect('langganan_view')
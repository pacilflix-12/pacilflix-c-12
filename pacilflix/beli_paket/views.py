from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection

@login_required
def show_beli_paket(request, paket_id):
    user_id = request.user.id

    # Get package details
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, nama, harga, resolusi_layar, dukungan_perangkat 
            FROM paket_langganan
            WHERE id = %s
        """, [paket_id])
        package = cursor.fetchone()

    if request.method == 'POST':
        metode_pembayaran = request.POST.get('metode_pembayaran')

        # Check if there is an active subscription
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id
                FROM transaksi
                WHERE user_id = %s AND end_date_time > NOW()
                ORDER BY end_date_time DESC
                LIMIT 1
            """, [user_id])
            active_subscription = cursor.fetchone()

        if active_subscription:
            # Update existing subscription
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE transaksi
                    SET paket_id = %s, start_date_time = NOW(), end_date_time = NOW() + INTERVAL '1 month'
                    WHERE id = %s
                """, [paket_id, active_subscription[0]])
        else:
            # Create new subscription
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO transaksi (user_id, paket_id, start_date_time, end_date_time)
                    VALUES (%s, %s, NOW(), NOW() + INTERVAL '1 month')
                """, [user_id, paket_id])

        return redirect('kelola_langganan_view')

    context = {
        'package': package,
    }

    return render(request, 'beli_paket.html', context)
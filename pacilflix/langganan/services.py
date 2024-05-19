from datetime import datetime, timedelta
from utils.query import select

def get_active_subscription(user: str) -> dict:
    query = f"""
        SELECT p.nama, p.harga, p.resolusi_layar, t.start_date_time, t.end_date_time
        FROM TRANSACTION t
        JOIN PAKET p ON t.nama_paket = p.nama
        WHERE t.username = '{user}' AND t.end_date_time > '{datetime.now()}'
        LIMIT 1
    """
    active_subscription = select(query)
    if active_subscription:
        paket = active_subscription[0]
        devices_query = f"""
            SELECT dukungan_perangkat
            FROM DUKUNGAN_PERANGKAT
            WHERE nama_perangkat = '{paket[0]}'
        """
        devices = [device[0] for device in select(devices_query)]
        return {
            "nama": paket[0],
            "harga": paket[1],
            "resolusi_layar": paket[2],
            "dukungan_perangkat": devices,
            "start_date_time": paket[3],
            "end_date_time": paket[4]
        }
    return {}

def get_available_packages() -> list:
    packages_query = "SELECT nama, harga, resolusi_layar FROM PAKET"
    packages = select(packages_query)
    available_packages = []
    for package in packages:
        devices_query = f"""
            SELECT dukungan_perangkat
            FROM DUKUNGAN_PERANGKAT
            WHERE nama_perangkat = '{package[0]}'
        """
        devices = [device[0] for device in select(devices_query)]
        available_packages.append({
            "nama": package[0],
            "harga": package[1],
            "resolusi_layar": package[2],
            "dukungan_perangkat": devices
        })
    return available_packages

def get_transaction_history(user: str) -> list:
    query = f"""
        SELECT t.nama_paket, t.start_date_time, t.end_date_time, t.metode_pembayaran, t.timestamp_pembayaran, p.harga
        FROM TRANSACTION t
        JOIN PAKET p ON t.nama_paket = p.nama
        WHERE t.username = '{user}'
        ORDER BY t.start_date_time DESC
    """
    history = select(query)
    transaction_history = [
        {
            "username": transaction[0],
            "start_date_time": transaction[1],
            "end_date_time": transaction[2],
            "nama_paket": transaction[3],
            "metode_pembayaran": transaction[4],
            "timestamp_pembayaran": transaction[5],
            "harga": transaction[6]
        }
        for transaction in history
    ]
    return transaction_history

def purchase_package(user: str, package_name: str, payment_method: str) -> None:
    end_date = datetime.now() + timedelta(days=30)
    query = f"""
        INSERT INTO TRANSACTION (username, start_date_time, end_date_time, nama_paket, metode_pembayaran, timestamp_pembayaran)
        VALUES (
            '{user}',
            '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}',
            '{end_date.strftime('%Y-%m-%d %H:%M:%S')}',
            '{package_name}',
            '{payment_method}',
            '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}'
        )
    """
    select(query)

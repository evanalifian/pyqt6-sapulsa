import sqlite3
connection = sqlite3.connect('penjualan_pulsa.sqlite')
cursor = connection.cursor()

# Aktifkan pengecekan foreign key di SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Data master
operators = [
    ('Telkomsel',),
    ('XL',),
    ('Indosat',),
    ('Tri',)
]

# (id_operator, nama_paket, jenis, harga_beli, harga_jual)
pakets = [
    (1, 'Pulsa 10.000', 'Pulsa', 10300, 11500),
    (1, 'Pulsa 25.000', 'Pulsa', 25300, 27000),
    (1, 'Data 5GB 30 Hari', 'Paket Data', 38000, 42000),
    (2, 'Pulsa 10.000', 'Pulsa', 10200, 11500),
    (2, 'Pulsa 50.000', 'Pulsa', 50400, 52500),
    (2, 'Data 10GB 30 Hari', 'Paket Data', 52000, 57000),
    (3, 'Pulsa 20.000', 'Pulsa', 20300, 22000),
    (3, 'Data 7GB 30 Hari', 'Paket Data', 40000, 44000),
    (4, 'Pulsa 15.000', 'Pulsa', 15200, 17000),
    (4, 'Data 12GB 30 Hari', 'Paket Data', 45000, 49000)
]

pelanggans = [
    ('Budi Santoso', '081234567801', 'Bangkalan'),
    ('Siti Aminah', '081234567802', 'Bangkalan'),
    ('Ahmad Fauzi', '081234567803', 'Sampang'),
    ('Dewi Lestari', '081234567804', 'Surabaya'),
    ('Rizky Pratama', '081234567805', 'Bangkalan')
]

kasirs = [
    ('Rina Kusuma', 'rina', 'rina123'),
    ('Doni Saputra', 'doni', 'doni123'),
    ('Maya Sari', 'maya', 'maya123')
]

# Data transaksi
# (id_transaksi, tanggal, id_pelanggan, id_kasir, total_bayar, metode_bayar, status)
transaksis = [
    ('TRX001', '2026-11-20 09:15:00', 1, 1, 11500, 'Tunai', 'Sukses'),
    ('TRX002', '2026-11-20 10:30:00', 2, 2, 65000, 'Transfer', 'Sukses'),
    ('TRX003', '2026-11-21 13:05:00', 3, 1, 52500, 'E-Wallet', 'Sukses'),
    ('TRX004', '2026-11-21 15:40:00', 1, 3, 39000, 'Tunai', 'Sukses'),
    ('TRX005', '2026-11-22 08:50:00', 4, 2, 57000, 'Transfer', 'Sukses'),
    ('TRX006', '2026-11-22 11:20:00', 5, 3, 54000, 'Tunai', 'Pending'),
    ('TRX007', '2026-11-23 09:00:00', 2, 1, 93000, 'E-Wallet', 'Sukses'),
    ('TRX008', '2026-11-23 10:10:00', 3, 2, 34500, 'Tunai', 'Gagal')
]

# (id_transaksi, id_paket, no_tujuan, jumlah, harga_satuan, subtotal)
details = [
    ('TRX001', 1, '081234567801', 1, 11500, 11500),
    ('TRX002', 3, '081234567802', 1, 42000, 42000),
    ('TRX002', 4, '081298765401', 2, 11500, 23000),
    ('TRX003', 5, '081234567803', 1, 52500, 52500),
    ('TRX004', 7, '081234567801', 1, 22000, 22000),
    ('TRX004', 9, '085712345678', 1, 17000, 17000),
    ('TRX005', 6, '081234567804', 1, 57000, 57000),
    ('TRX006', 2, '081234567805', 2, 27000, 54000),
    ('TRX007', 8, '081234567802', 1, 44000, 44000),
    ('TRX007', 10, '089912345678', 1, 49000, 49000),
    ('TRX008', 1, '081234567803', 3, 11500, 34500)
]

cursor.executemany("INSERT INTO operator (nama_operator) VALUES (?)", operators)
cursor.executemany("INSERT INTO paket (id_operator, nama_paket, jenis, harga_beli, harga_jual) VALUES (?, ?, ?, ?, ?)", pakets)
cursor.executemany("INSERT INTO pelanggan (nama_pelanggan, no_hp, alamat) VALUES (?, ?, ?)", pelanggans)
cursor.executemany("INSERT INTO kasir (nama_kasir, username, password) VALUES (?, ?, ?)", kasirs)
cursor.executemany("INSERT INTO transaksi (id_transaksi, tanggal, id_pelanggan, id_kasir, total_bayar, metode_bayar, status) VALUES (?, ?, ?, ?, ?, ?, ?)", transaksis)
cursor.executemany("INSERT INTO detail_transaksi (id_transaksi, id_paket, no_tujuan, jumlah, harga_satuan, subtotal) VALUES (?, ?, ?, ?, ?, ?)", details)
connection.commit()

cursor.execute("SELECT * FROM transaksi")
print(cursor.fetchall())
cursor.execute("SELECT * FROM detail_transaksi")
print(cursor.fetchall())
connection.close()

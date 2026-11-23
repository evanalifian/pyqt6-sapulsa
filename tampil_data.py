import sqlite3
connection = sqlite3.connect('penjualan_pulsa.sqlite')
cursor = connection.cursor()

# 1. Tampilkan isi setiap tabel
tabels = ['operator', 'paket', 'pelanggan', 'kasir', 'transaksi', 'detail_transaksi']

for tabel in tabels:
    print("Tabel", tabel)
    cursor.execute("SELECT * FROM " + tabel)
    for baris in cursor.fetchall():
        print(baris)
    print()

# 2. Tampilkan transaksi lengkap (gabungan beberapa tabel dengan JOIN)
print("Laporan Transaksi")
cursor.execute("""SELECT t.id_transaksi, t.tanggal, p.nama_pelanggan, k.nama_kasir,
t.total_bayar, t.metode_bayar, t.status
FROM transaksi t
JOIN pelanggan p ON t.id_pelanggan = p.id_pelanggan
JOIN kasir k ON t.id_kasir = k.id_kasir""")
for baris in cursor.fetchall():
    print(baris)
print()

# 3. Tampilkan rincian pembelian
print("Rincian Pembelian")
cursor.execute("""SELECT d.id_transaksi, o.nama_operator, pk.nama_paket,
d.no_tujuan, d.jumlah, d.subtotal
FROM detail_transaksi d
JOIN paket pk ON d.id_paket = pk.id_paket
JOIN operator o ON pk.id_operator = o.id_operator""")
for baris in cursor.fetchall():
    print(baris)

connection.close()

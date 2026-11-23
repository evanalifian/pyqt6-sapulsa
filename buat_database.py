import sqlite3
connection = sqlite3.connect('penjualan_pulsa.sqlite')
cursor = connection.cursor()

# Aktifkan pengecekan foreign key di SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Hapus tabel lama (tabel anak dihapus lebih dulu)
cursor.execute("DROP TABLE IF EXISTS detail_transaksi;")
cursor.execute("DROP TABLE IF EXISTS transaksi;")
cursor.execute("DROP TABLE IF EXISTS paket;")
cursor.execute("DROP TABLE IF EXISTS operator;")
cursor.execute("DROP TABLE IF EXISTS kasir;")
cursor.execute("DROP TABLE IF EXISTS pelanggan;")

cursor.execute("""CREATE TABLE pelanggan (
id_pelanggan INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
nama_pelanggan TEXT NOT NULL,
no_hp TEXT NOT NULL,
alamat TEXT)""")

cursor.execute("""CREATE TABLE kasir (
id_kasir INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
nama_kasir TEXT NOT NULL,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL)""")

cursor.execute("""CREATE TABLE operator (
id_operator INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
nama_operator TEXT NOT NULL)""")

cursor.execute("""CREATE TABLE paket (
id_paket INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
id_operator INTEGER NOT NULL,
nama_paket TEXT NOT NULL,
jenis TEXT NOT NULL,
harga_beli INTEGER NOT NULL,
harga_jual INTEGER NOT NULL,
FOREIGN KEY (id_operator) REFERENCES operator(id_operator))""")

cursor.execute("""CREATE TABLE transaksi (
id_transaksi TEXT PRIMARY KEY NOT NULL,
tanggal TEXT NOT NULL,
id_pelanggan INTEGER NOT NULL,
id_kasir INTEGER NOT NULL,
total_bayar INTEGER NOT NULL,
metode_bayar TEXT NOT NULL,
status TEXT NOT NULL,
FOREIGN KEY (id_pelanggan) REFERENCES pelanggan(id_pelanggan),
FOREIGN KEY (id_kasir) REFERENCES kasir(id_kasir))""")

cursor.execute("""CREATE TABLE detail_transaksi (
id_detail INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
id_transaksi TEXT NOT NULL,
id_paket INTEGER NOT NULL,
no_tujuan TEXT NOT NULL,
jumlah INTEGER NOT NULL,
harga_satuan INTEGER NOT NULL,
subtotal INTEGER NOT NULL,
FOREIGN KEY (id_transaksi) REFERENCES transaksi(id_transaksi),
FOREIGN KEY (id_paket) REFERENCES paket(id_paket))""")

connection.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
print(cursor.fetchall())
connection.close()

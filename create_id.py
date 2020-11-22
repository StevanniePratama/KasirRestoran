from datetime import datetime

def id_pesanan():
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day

	jam = hari_ini.hour
	menit = hari_ini.minute

	no_pesanan = "AAA"

	id_pesan = ("%04d%02d%02d - %s %02d%02d" % (tahun, bulan, hari, no_pesanan, jam, menit))
	return id_pesan

def id_member(nama):
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day

	id_pesan = ("%04d%02d%02d - %s" % (tahun, bulan, hari, nama))
	return id_pesan

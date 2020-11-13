from os import system
from time import sleep
from datetime import datetime
import random

list_pesanan = 

def id_pesanan():
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day

	no_pesanan = "001"

	id_pesan = ("%04d%02d%02d - %s" % (tahun, bulan, hari, no_pesanan))
	print(id_pesan)

def Tampilah_Awal():
	system("cls")
	print("""
	MEKDI Fast Food
	
	[1] Daftar Menu
	[2] CheckOut
	[3] Kartu Member
	[Q] Keluar

	""")


def Menu_paketan(pilih):
	system("cls")
	print("""
	[MENU PAKETAN]

	[1]	Paket 1				Rp25.000
		Ayam + Nasi + Es Teh

	[2]	Paket 2				Rp40.000
		2 Ayam + Nasi + Kentang Goreng + Es Teh

	[3]	Paket 3				Rp65.000
		3 Ayam + 2 Nasi + 2 Es Teh
	
	[4]	Paket 4				Rp90.000
		5 Ayam + 3 Nasi + 4 Es Teh

	[5] Paket 5				Rp150.000
		10 Ayam + 5 Nasi
	""")


def Paket_Pilihan(paket):
	if paket == "1":
		list_pesanan[pesanan] = {'Paket 1'}
	elif paket == "2" :
		pass

def Menu_Baru():
	print("V")

def Jenis_Menu(pilih) :
	if pilih == "1" :
		Menu_paketan()
	elif pilih == "2" :
		Menu_Baru()
	elif pilih == "3" :
		pass
	elif pilih == "4" :
		pass
	elif pilih == "5" :
		pass
	elif pilih == "6" :
		pass
	elif pilih == "7" :
		pass
	elif pilih == "8" :
		pass
	elif pilih == "9" :
		pass

def daftar_menu():
	system("cls")
	print("""
	DAFTAR MENU

	[1] Menu Paketan
	[2] Menu Terbaru
	[3] Burger
	[4] Ayam
	[5] Nasi
	[6] Mie
	[7] Snack
	[8] Minuman
	[9] Kids Meal

	""")

def memilih_menu():
	daftar_menu()
	User_pilihan = input("Pilihan : ").upper()
	Open = Jenis_Menu(pilih = User_pilihan)
	return Open

def check_pilihan(pilihan):
	if pilihan == "Q" :
		return False
	elif pilihan == "1" :
		memilih_menu()
		return True
	elif pilihan == "2" :
		pass
	elif pilihan == "3" :
		pass

def start() :
	Tampilah_Awal()
	user_input = input("Pilihan : ").upper()
	start = check_pilihan(pilihan = user_input)
	return start

start()


	





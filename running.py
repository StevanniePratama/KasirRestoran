import view
import pilihan
import json
import create_id
import os

def paket() :
	view.MenuPaketan()
	user_input = input()
	user_input2 = input("Jumlah : ")
	lanjut = pilihan.check_paket(pilihan = user_input, jumlah = user_input2)
	return lanjut

def baru():
	view.MenuTerbaru()
	user_input = input()
	user_input2 = input("Jumlah : ")
	lanjut = pilihan.check_baru(pilihan = user_input, jumlah = user_input2)
	return lanjut

def burger():
	view.MenuBurger()
	user_input = input()
	user_input2 = input()
	user_input3 = input("Jumlah : ")
	lanjut = pilihan.check_burger(pilihan = user_input, pilih = user_input2, jumlah = user_input3)
	return lanjut

def ayam():
	view.MenuAyam()
	user_input = input()
	user_input2 = input("Jumlah : ")
	lanjut = pilihan.check_ayam(pilihan = user_input, jumlah = user_input2)
	return lanjut

def nasi():
	view.MenuNasi()
	user_input = input()
	user_input2 = input()
	user_input3 = input("Jumlah : ")
	lanjut = pilihan.check_nasi(pilihan = user_input, pilih = user_input2, jumlah = user_input3)
	return lanjut

def mie():
	view.MenuMie()
	user_input = input()
	user_input2 = input("Jumlah : ")
	lanjut = pilihan.check_mie(pilihan = user_input, jumlah = user_input2)
	return lanjut

def snack():
	view.MenuSnack()
	user_input = input()
	user_input2 = input("Jumlah : ")
	lanjut = pilihan.check_snack(pilihan = user_input, jumlah = user_input2)
	return lanjut

def minuman():
	view.MenuMinuman()
	user_input = input()
	user_input2 = input()
	user_input3 = input("Jumlah : ")
	lanjut = pilihan.check_minuman(pilihan = user_input, pilih = user_input2, jumlah = user_input3)
	return lanjut

def sadmeal():
	view.MenuSadMeal()
	user_input = input()
	user_input2 = input("Jumlah : ")
	lanjut = pilihan.check_sadmeal(pilihan = user_input, jumlah = user_input2)
	return lanjut

def pilihMenu() :
	view.daftar_menu()
	user_input = input()
	lanjut = pilihan.check_menu(pilihan = user_input)
	return lanjut

def CheckOut() :
	view.print_data()
	print(pilihan.TotalHarga())

def KartuMember() :
	os.system("cls")
	user_input = input("Nama : ")
	save = create_id.id_member(nama = user_input)
	print(save)

def start() :
	view.main_menu()
	user_input = input()
	start = pilihan.check_main(pilihan = user_input)
	return start

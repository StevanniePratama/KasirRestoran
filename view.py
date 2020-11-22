import os 
import system 
import create_id
import pilihan

MenuPaketan = system.load_MenuSatu()
MenuTerbaru = system.load_MenuDua()
MenuBurger = system.load_MenuTiga()
MenuAyam = system.load_MenuEmpat()
MenuNasi = system.load_MenuLima()
MenuMie = system.load_MenuEnam()
MenuSnack = system.load_MenuTujuh()
MenuMinuman = system.load_MenuDelapan()
MenuSadMeal = system.load_MenuSembilan()

def main_menu() :
	os.system("cls")
	print(system.load_Main_Menu())

def daftar_menu() :
	os.system("cls")
	print(system.load_Daftar_Menu())

def MenuPaketan() :
	os.system("cls")
	print(system.load_MenuSatu())

def MenuTerbaru() :
	os.system("cls")
	print(system.load_MenuDua())

def MenuBurger() :
	os.system("cls")
	print(system.load_MenuTiga())

def MenuAyam() :
	os.system("cls")
	print(system.load_MenuEmpat())

def MenuNasi() :
	os.system("cls")
	print(system.load_MenuLima())

def MenuMie() :
	os.system("cls")
	print(system.load_MenuEnam())

def MenuSnack() :
	os.system("cls")
	print(system.load_MenuTujuh())

def MenuMinuman() :
	os.system("cls")
	print(system.load_MenuDelapan())

def MenuSadMeal() :
	os.system("cls")
	print(system.load_MenuSembilan())

listpesanan = system.load_List()

def print_data() :
	os.system("cls")
	for id_pesanan in listpesanan:
		nama = listpesanan["nama_barang"]
		harga = listpesanan["HargaTotal"]
		jumlah = listpesanan["jumlah"]
		print(id_pesanan)
		print(f"{nama}	Rp{harga}")
		print(f"x{jumlah}")
import view
import running
import system
import create_id
#import os

list_Pesanan = system.load_List()

TotalHarga = []

def check_paket(pilihan, jumlah):
	if pilihan == "1" :
		harga = 20000
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Paket 1",
				"jumlah" : "1",
				"HargaTotal" : "20.000"
				}
			saved = system.load_saveList()
			saved()
		if jumlah == "2" :
			harga = harga*2
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Paket 1",
				"jumlah" : "2",
				"HargaTotal" : "40.000"
				}
			saved = system.load_saveList()
			saved()
	
	if pilihan == "2" :
		harga = 32600
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Paket 2",
				"jumlah" : "1",
				"HargaTotal" : "32.600"
				}
			saved = system.load_saveList()
			saved()
		if jumlah == "2" :
			harga = harga*2
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Paket 2",
				"jumlah" : "2",
				"HargaTotal" : "65.200"
				}
			saved = system.load_saveList()
			saved()
	
	if pilihan == "3" :
		harga = 38500
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Paket 3",
				"jumlah" : "1",
				"HargaTotal" : "38.500"
				}
			saved = system.load_saveList()
			saved()
		if jumlah == "2" :
			harga = harga*2
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Paket 3",
				"jumlah" : "2",
				"HargaTotal" : "77.000"
				}
			saved = system.load_saveList()
			saved()
	if pilihan == "4" :
		harga = 99900
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Paket 4",
				"jumlah" : "1",
				"HargaTotal" : "99.900"
				}
			saved = system.load_saveList()
			saved()
		if jumlah == "2" :
			harga = harga*2
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Paket 4",
				"jumlah" : "2",
				"HargaTotal" : "199.800"
				}
			saved = system.load_saveList()
			saved()

	else :
		check_menu()

def check_baru(pilihan, jumlah):
	if pilihan == "1" :
		harga = 12400
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Cendol Dawet",
				"jumlah" : "1",
				"HargaTotal" : "12.400"
				}
			saved()
		if jumlah == "2" :
			harga = harga*2
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Cendol Dawet",
				"jumlah" : "2",
				"HargaTotal" : "24.800"
				}
			saved()
	
	if pilihan == "2" :
		harga = 8000
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Kopi Dangdut",
				"jumlah" : "1",
				"HargaTotal" : "8.000"
				}
			saved()
		if jumlah == "2" :
			harga = harga*2
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Kopi Dangdut",
				"jumlah" : "2",
				"HargaTotal" : "16.000"
				}
			saved()
	
	if pilihan == "3" :
		harga = 15100
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Cloud Bread",
				"jumlah" : "1",
				"HargaTotal" : "15.100"
				}
			saved()
		if jumlah == "2" :
			harga = harga*2
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Cloud Bread",
				"jumlah" : "2",
				"HargaTotal" : "30.200"
				}
			saved()
	if pilihan == "4" :
		harga = 10000
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Dalgona Coffee",
				"jumlah" : "1",
				"HargaTotal" : "10.000"
				}
			saved()
		if jumlah == "2" :
			harga = harga*2
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Dalgona Coffee",
				"jumlah" : "2",
				"HargaTotal" : "20.000"
				}
			saved()

	if pilihan == "5" :
		harga = 14400
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Korean Garlic Bread",
				"jumlah" : "1",
				"HargaTotal" : "14.400"
				}
			saved()
		if jumlah == "2" :
			harga = harga*2
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Korean Garlic Bread",
				"jumlah" : "2",
				"HargaTotal" : "28.800"
				}
			saved()

	else :
		check_menu()

def check_burger(pilihan, pilih, jumlah):
	pass

def check_ayam(pilihan, jumlah):
	pass

def check_nasi(pilihan, pilih, jumlah):
	pass

def check_mie(pilihan, jumlah):
	pass

def check_snack(pilihan, jumlah):
	if pilihan == "1" :
		harga = 15900
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Kentang Goreng",
				"jumlah" : "1",
				"HargaTotal" : "15.900"
				}
			saved = system.load_saveList()
			saved()
		if jumlah == "2" :
			pass
	
	if pilihan == "2" :
		harga = 14200
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Chicken Nugget",
				"jumlah" : "1",
				"HargaTotal" : "14.2000"
				}
			saved = system.load_saveList()
			saved()
		if jumlah == "2" :
			pass
	
	if pilihan == "3" :
		harga = 12000
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Garlic Rings",
				"jumlah" : "1",
				"HargaTotal" : "12.000"
				}
			saved = system.load_saveList()
			saved()
		if jumlah == "2" :
			pass

	if pilihan == "4" :
		harga = 12000
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "CornDog",
				"jumlah" : "1",
				"HargaTotal" : "12.000"
				}
			saved = system.load_saveList()
			saved()
		if jumlah == "2" :
			pass

	if pilihan == "5" :
		harga = 12400
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "Ice Cream Cake",
				"jumlah" : "1",
				"HargaTotal" : "12.400"
				}
			saved = system.load_saveList()
			saved()
		if jumlah == "2" :
			pass

	if pilihan == "6" :
		pass

	if pilihan == "7":
		pass

	else :
		check_menu()

def check_minuman(pilihan, pilih, jumlah):
	pass

def check_sadmeal(pilihan, jumlah):
	if pilihan == "1" :
		harga = 35000
		if jumlah == "1" :
			save = TotalHarga.append(harga)
			return save
			id_pesanan = create_id.id_pesanan()
			list_pesanan[id_pesanan] = {
				"nama_barang" : "SadMeal 1",
				"jumlah" : "1",
				"HargaTotal" : "35.000"
				}
			saved = system.load_saveList()
			saved()
		if jumlah == "2" :
			pass
	
	if pilihan == "2" :
		pass
	
	if pilihan == "3" :
		pass

	if pilihan == "4" :
		pass

def check_menu(pilihan):
	if pilihan == "1" :
		running.paket()
	elif pilihan == "2" :
		running.baru()
	elif pilihan == "3" :
		running.burger()
	elif pilihan == "4" :
		running.ayam()
	elif pilihan == "5" :
		running.nasi()
	elif pilihan == "6" :
		running.mie()
	elif pilihan == "7" :
		running.snack()
	elif pilihan == "8" :
		running.minuman()
	elif pilihan == "9" :
		running.sadmeal()
	else :
		check_main()

#def bayar():
	#os.system("cls")
	#satu = TotalHarga[0] 
	#dua = TotalHarga[1]
	#tiga = TotalHarga[2]
	#empat = TotalHarga[3]
	#lima = TotalHarga[4]
	#total = satu + dua + tiga + empat + lima 
	#user_input = input("Apakah Anda memiliki Kartu Member? ")
	#if user_input == "y" :
		#total1 = total - (10/100)
		#print(f"Total :		Rp{total1}")
	#elif user_input == "n" :
	#print(f"Total Pembayaran :		Rp{total}")

def bayar():
	satu = TotalHarga[0] 
	dua = TotalHarga[1]
	tiga = TotalHarga[2]
	total = satu + dua + tiga
	print(f"Total Pembayaran : Rp{total}")

def check_main(pilihan):
	if pilihan == "1" :
		running.pilihMenu()
	elif pilihan == "2" :
		bayar()
	elif pilihan == "3" :
		running.KartuMember()
	elif pilihan == "Q" :
		return False


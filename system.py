import system
from json import dump

path01 = "data/MenuSatu.txt"
path02 = "data/MenuDua.txt"
path03 = "data/MenuTiga.txt"
path04 = "data/MenuEmpat.txt"
path05 = "data/MenuLima.txt"
path06 = "data/MenuEnam.txt"
path07 = "data/MenuTujuh.txt"
path08 = "data/MenuDelapan.txt"
path09 = "data/MenuSembilan.txt"

path10 = "main/main_menu.txt"
path11 = "main/daftar_menu.txt"

path12 = "main/listpesanan.json"

mode = "r"
mode2 = "w"

def load_Main_Menu():
	with open(path10, mode) as file :
		data = file.read()
	return data

def load_Daftar_Menu():
	with open(path11, mode) as file :
		data = file.read()
	return data

def load_MenuSatu():
	with open(path01, mode) as file :
		data = file.read()
	return data

def load_MenuDua():
	with open(path02, mode) as file :
		data = file.read()
	return data

def load_MenuTiga():
	with open(path03, mode) as file :
		data = file.read()
	return data

def load_MenuEmpat():
	with open(path04, mode) as file :
		data = file.read()
	return data

def load_MenuLima():
	with open(path05, mode) as file :
		data = file.read()
	return data

def load_MenuEnam():
	with open(path06, mode) as file :
		data = file.read()
	return data

def load_MenuTujuh():
	with open(path07, mode) as file :
		data = file.read()
	return data

def load_MenuDelapan():
	with open(path08, mode) as file :
		data = file.read()
	return data

def load_MenuSembilan():
	with open(path09, mode) as file :
		data = file.read()
	return data

def load_List():
	with open(path12, mode) as file :
		data = file.read()
	return data

path13 = load_List()

def load_saveList():
	with open(path12, mode2) as file :
		dump(path12, file)

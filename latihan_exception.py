mobil = {'cr-v':"Honda",'ayla':"Daihatsu",'avanza':"Toyota"}
try:
	tipe = str(input("Masukan tipe mobil anda: "))
	print("Tipe Mobil Anda: {}".format(mobil[tipe]))
	tahun = int(input("Masukkan tahun rakitan mobil anda :"))
	print("Tahun rakit Mobil Anda: {}".format(tahun))

except KeyError:
	print("Tipe Mobil tidak tersedia!")	
except ValueError:
	print("Tahun rakitan harus angka!")
except KeyboardInterrupt:
	print("^CAnda mengakhiri program!")
# Variable dan Tipe Data
angka = 10
phi = 3.14
nama = "keziass"

# ini adalah program mengitung volume kubus
sisi = input("panjang sisi kubus")
Volume = 0

sisi = int(sisi)

Volume = sisi*sisi*sisi
print("volumenya adalah : ")
print(Volume)

# Concatinate dan escaping
NAMA_DEPAN = "kezia"
NAMA_belakng = "sindy"

NAMA_PANJANG = NAMA_DEPAN + " " + NAMA_belakng

print(NAMA_PANJANG)

# Percabangan Lampu jalan
gender = 2

if gender == 1 :
    print("kezia adalah laki-laki")
else:
    print("kezia adalah wanita")

lampu = "green" # green, yello, red

if lampu == "green":
    print("mobil jalan")
elif lampu == "yellow" :
    
    print("mobil pelan2")
else:
    
    print("mobil stop")

# Percabangan Nilai
nilai = 60

if nilai <60 :
    print("harus mengulang")
else:
    print("lulus")

# nilai < 90 dan nilai > 80  A
# nilai < 80 dan nilai > 70  B
# nilai < 70 dan nilai > 60  C
# D

nilai = 76
if nilai > 80 and nilai < 90:
    print("A")
elif nilai >70  and nilai < 80:
    print("B")
elif nilai >60 and nilai < 70:
    print("C")
else:
    print("D")

# jika nilai > 80 dan absen kurang dari 3 maka lulus selain itu remidi

nilai = 70
absen = 2

if nilai >80 and absen <3 :
    print("lulus")
else:
    print("tidak lulus")

# Menulis bilangan 10 sd 1
angka = 10

while angka >0 :
    print(angka)
    angka = angka - 1

# Menulis bilangan bulat dari 2 sd 10 
angka = 2
while angka <= 10:
    print(angka)
    angka = angka + 2

# Menulis bilangan bulat dari 2 sd 10
angka = 1
while angka <= 10:
    if (angka % 2) == 0:
        print(angka)
    angka = angka + 1

# Menulis bilangan ganjil dari 20 sd 0
angka = 20
while angka >= 0 :
    if (angka % 2) != 0:
        print (angka)
    angka = angka - 1

# Variable Tipe Data List
gender = ["laki-laki", "perempuan"]

print(gender[0])

# Mencetak list dengan mengguankan while
bulan = ["januari", "febuari", "maret"]

index = 0  
while index <= 2 :
    print (bulan[index])
    index += 1

print("*")
print("*" * 2)
print("*" * 3)

# Mencetak bintang membentuk segitiga
angka = 1
while angka <= 3 :
    print ("*" * angka)
    angka += 1

# Mencetak bintang dengan spasi
angka = 1
while angka <= 3:
    cetak = (" " * (3 - angka)) + ("*" * angka)
    print(cetak)
    angka += 1

# Mencetak bintang terbalik
angka = 3
while angka >=1 :
    print ("*" * (angka))
    angka -= 1

# Mencetak bintang terbalik dengan spasi
angka = 3
while angka >= 1:
    cetak = (" " * (3 - angka)) + ("*" * angka)
    print(cetak)
    angka -= 1

# Mencetak list dengan menggunakan for
bulans = ["januari", "febuari", "maret"]

for bulan in  bulans:
    print(bulan)
bulans[0] = 1
print(bulans[0])

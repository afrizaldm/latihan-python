# function menampilkan nama
def namasaya(nama):
    print(nama)
    return

namasaya("kezia")
namasaya("madiun")
namasaya("kasismatik")

# function perkalian dua angka
def kali(angka1, angka2):
    hasil = angka1 * angka2
    return hasil

print(kali(5, 5))
print(kali(5, 8))
print(kali(5, 10))

# function mencari volume balok
def volume(angka1, angka2, angka3) :
    hasil = angka1 * angka2 *angka3
    return hasil

print(volume(2,5,3))

# function mencari volume balok 2
def volume(angka) :
    hasil = angka[0] * angka[1] *angka[2]
    return hasil

i = [2,5,3]
print(volume(i))

# function membuat bintang
def bintang (max) :
    angka = 1
    while angka < max :
        print("*" * angka)
        angka = angka +1
    return

bintang (10)

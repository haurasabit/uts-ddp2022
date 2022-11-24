satu = input("Masukkan angka pertama = ")
dua = input("Masukkan angka kedua = ")
pilih = input("Pilih Operator : ")

tambah = "tambah"
kurang = "kurang"
bagi = "bagi"
kali = "kali"
pangkat = "pangkat"

if pilih == "tambah" :
    print (int(satu) + int(dua))
elif pilih == "kurang" :
    print (int(satu) - int(dua))
elif pilih == "bagi" :
    print (int(satu) / int(dua))
elif pilih == "kali" :
    print (int(satu) * int(dua))
elif pilih == "pangkat" :
    print (int(satu) ** int(dua))

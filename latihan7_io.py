print ("--------------------------")
print ("luas  bidang")
print ("pilih bidang",
       "\n 1. segitiga",
       "\n 2. lingkaran,"
       "\n 3. persegi panjang")

pilihan = int (input ("\n masukan pilihan : "))

#percabangan
if (pilihan == 1):
    alas = eval(input("masukan alas : "))
    tinggi = eval(input("masukan tinggi : "))

    #hitung luas segitiga
    hasil =alas * tinggi / 2
    print(f"hasil dari perhitungan luas segitiga adalah{hasil}")

elif (pilihan == 2):
    phi = 3.14
    r = eval(input("masukan r : "))

    #hitung luas lingkaran
    hasil =phi * r * r 
    print(f"hasil dari perhitungan luas lingkaran adalah{hasil}")

elif (pilihan == 3): 
    panjang = eval (input ("masukan panjang :"))
    lebar = eval (input ("masukan lebar : "))

    #hitung luas persegi panjang
    hasil = panjang * lebar
    print (f"hasil dari pergitungan luas persegi panjang adalah :{hasil}")

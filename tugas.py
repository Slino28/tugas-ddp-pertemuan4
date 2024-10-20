print("------------PT.GoldFish------------")
nama = input("Nama Pegawai : ")
divisi = input("Divisi : ")
agama = input("Agama : ")
jabatan = input("Jabatan : ")

#gaji pokok
if jabatan == "staff":
    gapok = 4000000
elif jabatan == "kabag":
    gapok = 7000000
elif jabatan == "manager":
    gapok = 10000000

#tunjab
tunjab = gapok * 0.2

#gaji kotor
gakot = gapok + tunjab

#zakat
zakat = gakot * 0.025 if agama == "islam" and gakot >= 7000000 else 0

#gaji bersih
gaji_bersih = gakot - zakat

#cetak
print ("\n-------------- Data Gaji---------------"
       f"\n Nama\t\t\t: {nama}",
       f"\n Agama\t\t\t: {agama}",
       f"\n Divisi\t\t\t: {divisi}"
       f"\n Jabatan\t\t: {jabatan}"
       f"\n Gaji Pokok\t\t: {gapok:,}"
       f"\n Tunjangan Jabatan\t: {tunjab:,}"
       f"\n Gaji Kotor\t\t: {gakot:,}"
       f"\n Zakat\t\t\t: {zakat:,}"
       f"\n Gaji Bersih\t\t: {gaji_bersih:,}")
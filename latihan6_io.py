nama =input ("nama mahasiswa \t: ")
bb = float (input("berat badan\t: "))
tb = float (input("tinggi badan\t: "))
fisik = str ("")
imt = bb/(tb ** 2)

if imt > 0 and imt <18.5 : fisik = "kurus"
elif imt >= 18.5 and imt < 25 : fisik = "normal"
elif imt >= 25 and imt < 30 : fisik = "overweight"
elif imt >= 30 : fisik = "obesitas"
else : imt = "kurang gizi"

#cetak
print ("nama mahasiswa \t: %s"
       "\n berat badan \t : %.2f"
       "\n tinggi badan \t : %.2f"
       "\n imt \t\t : %.2f"
       "\n kondisi fisik : %s" %  (nama,bb,tb,imt,fisik))


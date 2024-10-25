#belajar io & format print
a1 = int (input ("masukan angka 1:"))
a2 = int (input ("masukan angka 2:"))
hasil = a1*a2
#cetak
print (a1,"x",a2,"=",hasil)
print ("%i x %i = %i" %(a1,a2,hasil))

#belajar io
a1 = int (input ("masukan angka 1:"))
a2 = float (input ("masukan angka 2:"))
hasil = a1*a2
#cetak
print ("%i x %.2f = %.2f"%(a1,a2,hasil))
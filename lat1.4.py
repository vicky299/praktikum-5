#no.4
print("STRUK RINCIAN GAJI KARYAWAN")
namakaryawan = nama = input("nama karyawan :")
golongan     = gol = input("masukkan golongan :")


if(golongan=="A"):
    print("gol A")
    print("gaji pokok : 10000000")
    print("potongan : 10000000*2.5/100 = 250000")
    print("gaji bersih : 9750000")
elif(golongan== "B"):
    print("Gol B")
    print("gaji pokok : 8500000")
    print("potongan : 8500000*2/100 = 170000")
    print("gaji bersih : 8330000")
elif (golongan== "C"):
    print("gol C")
    print("gaji pokok : 7000000")
    print("potongan : 7000000*1.5/100 = 105000")
    print("gaji bersih : 6895000")
elif (golongan== "D"):
    print("gol D")
    print("gaji pokok : 5500000")
    print("potongan : 5500000*1/100 = 55000")
    print("gaji bersih : 5445000")
else :
    print ("tidak masuk golongan")



     

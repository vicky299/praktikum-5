#no.4
print("STRUK RINCIAN GAJI KARYAWAN")
namakaryawan = nama = input("nama karyawan :")
golongan     = gol = input("masukkan golongan :")

if(gol=='A'):
    gajipokok=10000000
    potongan=(2.5)/100
if(gol=='B'):
    gajipokok=8500000
    potongan=(2.0)/100
if(gol=='C'):
    gajipokok=7000000
    potongan=(1.5)/100
if(gol=='D'):
    gajipokok=5500000
    potongan=(1.0)/100

potonganfix=int(potongan*gajipokok)
print('gaji pokok   : ', gajipokok)
print('potongan     : ', potongan)
print('gaji bersih  : ', gajipokok - potonganfix)


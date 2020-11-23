#no.5
kode=input('Masukkan kode karyawan:')
nama=input('Masukkan nama karyawan:')
gol=input('Masukkan golongan:')
status=input('Masukkan status(1: menikah, 2:belum menikah)     :')
if (status=='menikah'):
    anak=int(input('masukkan jumlah anak     '))
if(status=='belum menikah'):
    anak=0


if(gol=='A')or (gol=='a'):
    gajipokok=10000000
    potongan=(2.5)/100
if(gol=='B')or (gol=='b'):
    gajipokok=8500000
    potongan=(2.0)/100
if(gol=='C')or (gol=='c'):
    gajipokok=7000000
    potongan=(1.5)/100
if(gol=='D')or(gol=='d'):
    gajipokok=5500000
    potongan=(1.0)/100
if(status=='menikah'):
    tunjanganpasutri= (10/100)*gajipokok
    if(anak>0):
        tunjangananak=((5/100)*gajipokok)*anak
potonganfix=potongan*gajipokok
if(status=='belum menikah'):
    gajikotor=gajipokok
if(status=='menikah'):
    gajikotor=gajipokok+tunjanganpasutri
    if(anak>0):
        gajikotor=gajipokok+tunjanganpasutri+tunjangananak


potonganfix=int(potongan*gajipokok)
print('gaji pokok   : ', gajipokok)
print('potongan     : ', potongan)
print('gaji kotor   : ', gajikotor)
print('gaji bersih  : ', gajikotor - potonganfix)

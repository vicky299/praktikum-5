from random import randint
bil=randint(0,100)
print("poin anda 100 dan akan berkurang 2 apabila salah")
print("Hai.. nama saya Mr. handsome, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
while True:
    tbkn=int(input("Tebakan Anda  : "))
    poin = 100
    if(tbkn<0) or (tbkn>100):
        print("error!!!")
        exit()
    if(tbkn>bil) and (tbkn>0) and (tbkn<100):
        print("Hehehe... Bilangan tebakan anda terlalu besar")
        False
    if(tbkn<bil) and (tbkn>0) and (tbkn<100):
        print("Hehehe... Bilangan tebakan anda terlalu kecil")
        False
    if(tbkn==bil):
        print("Yeeee... Bilangan tebakan anda BENAR :-)")
        True
        break
n=100
x=-2
if(False):
    print('nilai anda:', n+(x*False))

    




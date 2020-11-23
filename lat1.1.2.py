#latihan praktikum 1

#no.1

#syarat kelulusan
#tidak ada nilai yang kurang dari 60
#nilai matematika harus lebih dari 70

print("status kelulusan siswa")
print ("range(1-100)")
nilaibindo = a =int(input("masukkan nilai bahasa Indonesian :"))
nilaiIpa   = b =int(input("masukkan nilai IPA :"))
nilaimat   = c =int(input("masukkan nilai matematika :"))

if (60<=a<=100) and (60<=b<=100) and (70<=c<=100):
    print("LULUS")

elif ( 0<a<60) or (0<b<60) or (0<c<70):
    print("TIDAK LULUS")
          

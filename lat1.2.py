#latihan praktikum 1

#no.3

#syarat kelulusan
#tidak ada nilai yang kurang dari 60
#nilai matematika harus lebih dari 70

print("status kelulusan siswa")
print ("range(1-100)")
nilaibindo = a =int(input("masukkan nilai bahasa Indonesian :"))
nilaiIpa   = b =int(input("masukkan nilai IPA :"))
nilaimat   = c =int(input("masukkan nilai matematika :"))

if (a>=60) and (b>=60) and (c>70):
    print("LULUS")

elif ( a<60) or (b<60) or (c<70):
    print("TIDAK LULUS")
    print ("sebab")
    print("Nilai bahasa Indonesia kurang dari 60") or ("Nilai matematikanya kurang dari 70") 



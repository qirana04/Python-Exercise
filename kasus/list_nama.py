# #CONTOH SALAH:
# nama = 'aden'
# nama = 'putra'

# #ARRAY = CONTOH 1 FARIABLE TPI BISA JADI BNYAK
# #contoh yng bener

#fariable
nama = ['ADEN','PUTRA','FADHIL']

print(nama)
# #pengen manggil yang pertama
print(nama[0])
# #manggil yang yang ke2
print(nama[2])

# #cara merubah nama 
nama[0] = 'aden fahri athoriq'

# #kalu mau nambahin nama 
nama.append('alifka')

# #tampilkan semua menggunakan
for data in nama:
    print(data)

# #agar ada angka nya jadi berurutan
for i,x in enumerate(nama):
    print(i, '.', x)

#bisa juga kalau pengen di mulai dari angka misal 1
for i,x in enumerate(nama):
    print(i+1, '.', x)
print("======================================================")
print("\t\tRUMUS PRISMA SEGITIGA")
print("======================================================")

luas_alas =int(input("masukkan luas_alasnya\t: "))
luas_selimut =int(input("masukkan luas_selimut\t: "))
tinggi =int(input("masukkan tinggi\t: "))

luas = (2 * (luas_alas) + (luas_selimut))
volume = (luas_alas * tinggi)

print("luasnya adalah\t: ",luas)
print("volumenya adalah: ",volume)
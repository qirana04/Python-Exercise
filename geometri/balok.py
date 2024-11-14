print("=========================================")
print("\t\tRUMUS BALOK")
print("=========================================")

p =int(input("masukkan panjangnya\t: "))
l =int(input("masukkan luasnya\t: "))
t =int(input("masukkan tingginya\t: "))
pl =int(input("masukkan panjang_luasnya\t: "))
pt =int(input("masukkan panjang_tingginya\t: "))
lt =int(input("masukkan luas_tingginya\t\t: "))

volume = (p * l * t)
luas = (2 * (pl + pt + lt))

print("volumenya adalah: ",volume)
print("luasnya adalah\t: ",luas)
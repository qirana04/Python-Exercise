print("===================================")
print("\tprogram tabung")
print("===================================")

jari_jari = int(input("masukan nilai jari_jari: "))
phi = 3.14
tinggi = int(input("masukan nilai tinggi: "))

volume = 2 * phi * jari_jari * tinggi
luas_permukaan = phi * jari_jari + 2 * phi * jari_jari * tinggi

print('volume nya adalah =', volume, 'cm2')
print('luas permukaan nya adalah =', luas_permukaan, 'cm')
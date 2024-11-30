print("="*45)
print("\t\tRUMUS TABUNG")
print("="*45)

PHI = 3.14
r = int(input('Masukkan jari-jarinya\t : '))
t = int(input('Masukkan tingginya\t : '))

lp = (2 * PHI * r * r) + (2 * PHI * r ** 2)
ls = 2 * PHI * r * t
la_tinggi = PHI * r ** 2 * t

print('luas permukaan\t\t: ', lp)
print('luas selimut\t\t: ', ls)
print('luas alas x tinggi\t: ', la_tinggi)

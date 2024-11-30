#menentukan nilai sebuah angka
angka = int(input("Masukan angka\t: "))

if 100 <= angka < 1000:
    print('angka termasuk ratusan')
elif 1000 <= angka < 1000000:
    print('angka termasuk ribuan')
elif 1000000 <= angka < 100000000:
    print('angka termasuk jutaan')
else:
    print('angka melebihi batas')
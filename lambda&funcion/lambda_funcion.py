#contoh funcion
def persegi():
    sisi = int(input('sisi\t\t: '))
    luas = lambda s: s * s
    keliling = lambda s: 4 * s

    print('luas\t\t: ',luas(sisi), 'cm2')
    print('keliling\t: ',keliling(sisi), 'cm')

#bisa diulang bebas mau berapa
persegi()

#contoh ke 2
def nama_fungsi(nama,pesan):
    print(nama, '', pesan)

nama_fungsi('budi','selamat pagi')

#contoh lambda
rata2 = lambda nilai1,nilai2,nilai3: (nilai1 + nilai2 + nilai3)/3

print(rata2(90,88,76))
print(rata2(20,68,56))
print(rata2(90,88,56))

#bisa juga seperti ini
rata2 = lambda nilai1,nilai2,nilai3: (nilai1 + nilai2 + nilai3)/3
n1 = int(input('nilai1: '))
n2 = int(input('nilai2: '))
n3 = int(input('nilai3: '))
print(rata2(n1,n2,n3))
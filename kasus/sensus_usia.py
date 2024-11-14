# TUGAS
# buat aplikasi sensus usia 
# jumlah penduduk yang diinput ditanyakan
# input usia berdasaran jumlah penduduk tersebut
# cari rata-rata usia di penduduk tersebut
# cari usia tertua pertama dan kedua 
# cari usia termuda pertama dan kedua
# hitung data usia untuk masing2 usia

usia = []
tertua = []
termuda = []
penduduk = int(input('jumlah penduduk yang diinput: '))

for i in range(penduduk):
    usia.append(int(input(f'usia ke-{i+1} : ')))

total = 0
max1 = max2 = 0 # sama aja kaya total = 0 di bwahnya max = 0
min1 = min2 = 1000

for jumlah in usia:
    total += jumlah
    if jumlah > max1:
        max2 = max1
        max1 = jumlah
    elif jumlah > max2:
        max2 = jumlah

for jumlah in usia:
    if jumlah < min1:
        min2 = min1
        min1 = jumlah
    elif jumlah < min2:
        min2 = jumlah
rata_rata = jumlah / penduduk

print(f'\nrata-rata usia: {rata_rata} ')
print(f'usia tertua1: {max1} Tahun')
print(f'usia tertua2: {max2} Tahun')
print(f'usia termuda1: {min1} Tahun')
print(f'usia termuda2: {min2} Tahun')
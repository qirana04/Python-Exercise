#bikin arry kosong
nilai = []
jumlah = int(input('jumlah data yang akan diinput: '))

for i in range(jumlah):
    nilai.append(float(input(f'nilia ke-{i+1} : ')))

#perhitungan data di list
total = max = 0 # sama aja kaya total = 0 di bwahnya max = 0
min = nilai[0]
for data in nilai:
    total += data #sama ada kaya total = total + data
    if data > max:
        max = data

    if data < min:
        min = data

print(total)
print(f'jumlah total/t: {jumlah} ')
print(f'nilai terbesar: {max}')
print(f'nilai terkecil: {min}')


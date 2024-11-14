#buat list nama-nama bulan
#fariable
bulan = ['januari','februari','maret','april','mei','juni','juli','agustus','september','oktober','november','september','desember']

#tampilakn bulan maret dan oktober
print(bulan[2])
print(bulan[9])

#ganti bulan agustus dengan august dan ganti bulan januari dengan january
bulan[7] = 'august'
bulan[0] = 'january'

print(bulan)

#tambahkan bulan muhharam di list bulan
bulan.append('muhharam')

print(bulan)

#tampilkan semua nama bulan dengan format ada angka ny
#dan harus tampilan seperti:
#bulan ke-1 yaitu january

for i,x in enumerate(bulan):
    print(f'bulan ke-{i+1} yaitu {x}')

print("="*40)
print("\t\tKASUS")
print("="*40)

golongan = (input('Masukkan golongannya\t: '))
jam_kerja = int(input('Masukkan jamnya\t\t: '))

if golongan == 'A' :
    upah_per_jam = 4000
elif golongan == 'B' :
    upah_per_jam = 4000
elif golongan == 'C' :
    upah_per_jam = 4000
elif golongan == 'D' :
    upah_per_jam = 4000
total_upah = jam_kerja * upah_per_jam

if jam_kerja - 24 > 0:
    total_upah = total_upah + ((jam_kerja - 24)*4000)
    print('hasil upah pekerja lembur\t: ', 'RP' , total_upah )

print('hasilnya upah bersih\t: ', 'RP' , total_upah + (jam_kerja))

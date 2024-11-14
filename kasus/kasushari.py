print("="*40)
print("\tKASUS HARI,BULAN, TAHUN")
print("="*40)

hari_awal = int(input("masukan hari: "))

tahun = int(hari_awal / 365)
bulan = int((hari_awal - (tahun * 365))/30)
hari = int(hari_awal - tahun * 365 - bulan * 30)

print(f"\t{tahun}, TAHUN")
print(f"\t{bulan}, BULAN")
print(f"\t{hari}, HARI")
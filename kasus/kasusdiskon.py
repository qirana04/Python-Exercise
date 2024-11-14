print("="*45)
print("\t\tKASUS DISKON")
print("="*45)

total = int(input('masukan total belanja\t: '))
setelah_diskon = total
 
if total < 100000:
    diskon = total * (5/100)
else:
    diskon = total * (10/100)
 
setelah_diskon = total - diskon
print("Diskonya adalah\t\t: Rp {:,}".format(int(diskon)).replace(',','.'))
print("Harga setelah diskon\t: Rp {:,}".format(int(setelah_diskon)).replace(',','.'))
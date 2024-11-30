total_belanja = float(input("masukkan harga total belanja: "))
diskon = 0

if total_belanja >= 1000000:
    diskon = 6  / 100 * total_belanja
elif total_belanja >= 500000:
    diskon = 4/ 100 * total_belanja
elif total_belanja >= 100000:
    diskon = 2 / 100 * total_belanja

total_bayar = total_belanja - diskon

print(f'''
harga beli      : {total_belanja}
diskon          : {diskon}
dibayar         : {total_bayar}
''')
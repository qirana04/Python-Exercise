ukuran_sepatu = int(input("masukkan ukuran sepatu: "))


if ukuran_sepatu >= 40 and ukuran_sepatu <= 45:
    print("BESAR")
elif ukuran_sepatu >= 35 and ukuran_sepatu <= 40:
    print("SEDANG")
elif ukuran_sepatu >= 30 and ukuran_sepatu <= 35:
    print("KECIL")

else:
    print("ukuran sepatu salah")
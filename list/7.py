#program list buku

list_buku = []
while True:
    print("\nMasukan data buku")
    judul = input("Judul Buku\t\t: ")
    penulis = input("Masukan Nama Penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print('Nomor.\t\t| Judul\t\t| Penulis ')
    print("\n\n","="*15,"Data buku","="*15)
    for index,buku in enumerate(list_buku):
        print(f"{index+1}\t\t| {buku[0]}\t\t| {buku[1]} ")
    
    print("\n\n","="*20)
    Lanjut = input("Apakah mau lanjut?(y/n)")

    if Lanjut == "n":
        break

print("SELESAI")
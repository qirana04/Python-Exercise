# nomor 14
angka = 5
for x in range(angka):
    for y in range(x+1):
        print("*", end="")
    if x+1 == angka:
        print("*", end="")
        print("*", end="")
    print()


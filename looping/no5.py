# nomor 5
jumlah = 0
for number in range(1,6):
    if number < 5:
        print(number, "+", end= " ")
    else:
        print(number, end = " = ")  
    jumlah = jumlah + (number)
print(jumlah)
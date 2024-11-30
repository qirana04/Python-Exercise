#Menjumlahkan semua angka dalam daftar yang lebih besar dari 7
numbers = [3, 5, 9, 16, 21, 44, 78]
total = 0
for number in numbers:
    if number > 7:
        total += number
print("Total:", total)

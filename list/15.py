#menyaring list menjadi list genap saja
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered)

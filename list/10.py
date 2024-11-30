#mencari element yg sering muncul
list = [1, 2, 3, 1, 2, 1, 4, 2, 2, 3, 1, 4, 2, 4, 1, 2]
most_frequent = max(set(list), key=list.count)
print(most_frequent)

#menentukan panjang sebuah kata
kata = "apa"
if len(kata) > 5:
    print(f"{kata} memiliki panjang lebih dari 5 karakter")
elif len(kata) < 5 :
    print(f"{kata} memiliki panjang kurang dari 5 karakter")
else:
    print(f"{kata} memiliki panjang 5 karakter")

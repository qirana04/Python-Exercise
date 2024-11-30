#menentukan karakter huruf atau angka
char = 'A'
if char.isalpha():
    print(f"{char} adalah huruf")
elif char.isdigit():
    print(f"{char} adalah angka")
else:
    print(f"{char} bukan huruf atau angka")

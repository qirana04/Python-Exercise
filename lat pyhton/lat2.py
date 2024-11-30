status_lampu = input("status lampu: ").lower()
warna_lampu = input("masukan warna lampu lalu lintas: ").lower()

if status_lampu == 'menyala':
    if warna_lampu == 'merah':
        print('Berhenti!')
    elif warna_lampu == 'kuning':
        print('Bersiap!')
    elif warna_lampu == 'hijau':
        print('Maju!')
    else: 
        print('Warna salah!')
else:
    print('Jalan')
def persegi_panjang():
    
    p = int(input("masukan panjang: "))
    l = int(input("masukan lebar: "))

    keliling = lambda p,l: 2 * p + l 
    luas = lambda p,l: p * l

    print('keliling', keliling(p,l), 'cm')
    print('luas', luas(p,l), 'cm2')

persegi_panjang()
persegi_panjang()
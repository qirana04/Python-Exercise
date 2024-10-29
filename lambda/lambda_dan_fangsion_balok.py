def balok():
    p =int(input("masukkan panjangnya\t: "))
    l =int(input("masukkan luasnya\t: "))
    t =int(input("masukkan tingginya\t: "))
    pl =int(input("masukkan panjang_luasnya\t: "))
    pt =int(input("masukkan panjang_tingginya\t: "))
    lt =int(input("masukkan luas_tingginya\t\t: "))

    volume = lambda p,l,t,pl,pt,lt: p * l * t
    luas = lambda p,l,t,pl,pt,lt: 2 * pl + pt + lt

    print('volume', volume(p,l,t,pl,pt,lt), ' ')
    print('luas', luas(p,l,t,pl,pt,lt), 'cm2')

balok()
balok()
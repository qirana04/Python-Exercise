PHI = 3.14
def lingkaran():
    jp =int(input("masukkan jari-jari perseginya\t: "))
    luas = lambda jp: 3.14 * jp
    keliling = lambda jp: 2 * 3.14 * jp

    print('luas', luas(jp), 'cm2')
    print('keliling', keliling(jp), 'cm')

lingkaran()
lingkaran()

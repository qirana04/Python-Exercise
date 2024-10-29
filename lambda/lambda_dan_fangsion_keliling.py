PHI = 3.14
def keliling():
    jari2 = int(input('masukkan jari2: '))
    keliling = lambda j : 2 * PHI * jari2
    luas = lambda j : PHI * jari2 ** 2

    print('keliling', keliling(jari2), 'cm')
    print('luas', luas(jari2), 'cm2')

keliling()
keliling()
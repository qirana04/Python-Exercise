def kubus():
    r = int(input('masukan rusuknya: '))
    luas = lambda r: 6*r*r
    volume = lambda r: r*r*r

    print('luas', luas(r), 'cm2')
    print('volume', volume(r), ' ')

kubus()
kubus()
PHI = 3.14
def tabung():
    jari2 = int(input('masukkan jari2: '))
    tinggi = int(input('masukkan tinggi: '))
    lp= lambda j,t: 2 * PHI * j * t 

    print('luas persegi adalah: ', lp(jari2,tinggi), 'cm2')

tabung()
tabung()
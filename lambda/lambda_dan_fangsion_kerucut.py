PHI = 3.14
def kerucut():
    jp =int(input("masukkan jari2_perseginya\t: "))
    tinggi =int(input("masukkan tingginya\t\t: "))
    j2 =int(input("masukkan jari2nya\t\t: "))
    s =int(input("masukkan sisinya\t\t: "))

    volume = lambda jp,tinggi,j2,s: 1/3 * 3.14 * jp * tinggi
    luas = lambda jp,tinggi,j2,s: 3.14 * j2 * j2 + s

    print('volume', volume(jp,tinggi,j2,s), ' ')
    print('luas', luas(jp,tinggi,j2,s), 'cm2')

kerucut()
kerucut()
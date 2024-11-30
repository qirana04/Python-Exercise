predikat_nilai = int(input("masukkan nilai: "))

if predikat_nilai >= 90 and predikat_nilai <= 100:
    print("A")
elif predikat_nilai >= 80 and predikat_nilai<= 89:
    print("B")
elif predikat_nilai>= 70 and predikat_nilai<= 79:
    print("C")
elif predikat_nilai >= 60 and predikat_nilai<= 69:
    print("D")
elif  predikat_nilai < 60:
    print("E")
else: 
    print("nilai salah")

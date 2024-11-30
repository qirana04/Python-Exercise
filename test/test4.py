print("="*50)
print("\tmenentukan kelulusan dari 4 kriteria")
print("="*50)

karakter = input("masukan karakter: ").lower()

nilai_MTK = int(input("masukan nilai mtk: "))
nilai_b_indo = int(input("masukan nilai b indo: "))
nilai_b_ingg = int(input("masukan nilai b ingg: "))

if karakter == 'A' or karakter == 'B' and nilai_MTK >= 60 and nilai_b_indo >= 70 and nilai_b_ingg >= 55:
    print("lulus")

else:
    print("tidak lulus")
print('''
   silahkan pilih tools dibawah ini dengan mengirimkan nomornya
      =============================================
      tools yang tersedia
      =============================================
      1. Menghitung luas persegi
      2. Menghitung luas lingkaran
      3. Menghitung luas segetiga
      =============================================   
''')
a = int(input("pilihan :"))

match a:
    case 1:
        luaspersegi = int(input(" nilai sisi : "))
        hasilluas = luaspersegi * luaspersegi
        print("luas persegi adalah : ", hasilluas )
    case 2:
        nilaiphi = float(input("nilai phi : "))
        nilaijari = int(input(" nilai jari jari : "))
        jarijari = nilaijari * nilaijari
        luaslingkaran = nilaiphi * jarijari
        print("luas lingkaran adalah : ", luaslingkaran)
    case 3:
        rumus = float(0.5)
        alas = int(input(" nilai alas : "))
        tinggi = int(input(" nilai tinngi : "))
        hasilluas = rumus * alas * tinggi
        print("luas segitiga adalah : ", hasilluas)
    case _:
        print("angkanya salah")

            
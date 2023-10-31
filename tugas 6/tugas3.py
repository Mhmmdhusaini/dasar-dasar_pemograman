jumlahbaris = int(input("masukan jumlah baris: " ))

for i in range(1, jumlahbaris + 1):
    for h in range(i):
        print("*", end="")
    print()
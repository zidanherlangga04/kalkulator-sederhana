print("=" * 30)
print("Kalkulator Sederhana")
print("=" * 30)
print("Operasi bilangan\n")         # pilihan operasi bilangan
print(" 1. Pertambahan \t [+]")
print(" 2. Pengurangan \t [-]")
print(" 3. Perkalian   \t [*]")
print(" 4. Pembagian   \t [/]")
print("=" * 30)

operasi = input("Masukan operasi (1/2/3/4): ")        # user memilih operasi (+, -, *, dan /)
bilangan1 = eval(input("\nMasukan bilangan 1: "))     # awal bilangan
bilangan2 = eval(input("Masukan bilangan 2: "))       # akhir bilangan

# pencabangan jika user memilih satu dari yang lain
if operasi == "1":
    print("User memilih pertambahan")
elif operasi == "2":
    print("User memilih pengurangan")
elif operasi == "3":
    print("User memilih perkalian")
elif operasi == "4":
    print("User memilih pembagian")
else:
    print("Invalid")

# output yang di keluarkan dari pencabangan jika user memilih salah satu dari operasi (+, -, *, /)
if operasi == "1":
    hasil = bilangan1 + bilangan2
    print(f"Hasil dari {bilangan1} + {bilangan2} = {hasil}")    # hasil dari jumlah angka yang di tambah [+]
elif operasi == "2":
    hasil = bilangan1 - bilangan2
    print(f"Hasil dari {bilangan1} - {bilangan2} = {hasil}")    # hasil dari jumlah angka yang di kurang [-]
elif operasi == "3":
    hasil = bilangan1 * bilangan2
    print(f"Hasil dari {bilangan1} * {bilangan2} = {hasil}")    # hasil dari jumlah angka yang di kali [*]
elif operasi == "4":
    hasil = bilangan1 / bilangan2
    print(f"Hasil dari {bilangan1} / {bilangan2} = {hasil}")    # hasil dari jumlah angka yang di bagi [/]
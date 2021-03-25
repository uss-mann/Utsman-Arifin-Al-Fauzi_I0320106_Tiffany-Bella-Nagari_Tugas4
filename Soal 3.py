#program untuk memeriksa beban bagasi
batas_berat_bagasi = 50
konversi_kg_ke_pon = 2.205

print("PERIKSA BERAT BAGASI ANDA DISINI")
satuan = input("Pilih satuan:\n1. imperial(pon)\n2. metrik(kilogram)\npilihan:")
if satuan == '1':
    berat_bagasi = float(input("Masukkan berat bagasi(lbs):"))
elif satuan == '2':
    berat_bagasi = konversi_kg_ke_pon * float(input("Masukkan berat bagasi(kg):"))
else:
    print("Input tidak dikenal")
    exit()
if berat_bagasi>batas_berat_bagasi:
    print ("Berat bagasi TIDAK diperbolehkan. Harap kurangi beban.")
else:
    print ("Berat bagasi DIPERBOLEHKAN. Selamat menikmati penerbangan anda.")

#memeriksa poin a dan b
a = 110
b = 49

print("\n\na. Untuk beban lebih dari 110 kg:",a * konversi_kg_ke_pon < 50, ". Bagasi tidak diperbolehkan")
print("b. Untuk beban 49 kg:",b * konversi_kg_ke_pon < 50, ". Bagasi tidak diperbolehkan")
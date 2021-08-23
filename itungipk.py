print("=============================================")
print("|                                           |")
print("|      MENGHITUNG IPK & IPS MAHASISWA       |")
print("|                                           |")
print("=============================================")
print("|  >>> Selamat Datang di Portal UNUGHA <<<  |")
print("---------------------------------------------")

# Input Identitas
nama = input("| Nama Mahasiswa : ")
nim = input("| NIM Mahasiswa  : ")
semester = int(input("| Anda Semester  : "))
print("---------------------------------------------\n")

print("\n+++++++++++++++++++++++++++++++++++++++++++++")

# Prosedural
total_bobot = 0
total_sks = 0
a = 1
while a <= semester:
	print("<< Semester ke-{0} >>".format(a))
	jumlah_sks = int(input("| Jumlah SKS     : "))
	bobot_sks = float(input("| Bobot SKS      : "))
	ips = bobot_sks / jumlah_sks
	print("---------------------------------------------")
	print("Indeks Prestasi Semester (IPS) : {:.02f}".format(ips))
	print("---------------------------------------------")
	a += 1
	total_bobot += bobot_sks
	total_sks += jumlah_sks

ipk = total_bobot / total_sks
# Kartu Hasil Studi (KHS)
print("\n\n=============================================")
print("|        ---- Kartu Hasil Studi ----        |")
print("=============================================")
print("| Nama Mahasiswa : ", nama)
print("| NIM Mahasiswa  : ", nim)
print("| Semester       : ", semester)
print("---------------------------------------------")
print("| Total seluruh bobot   :", total_bobot)
print("| Total seluruh SKS     :", total_sks)
print("| IPK Selama {0} Semester : {1:.02f}".format(semester, ipk))
print("---------------------------------------------")
## Keterangan
if ipk >= 3.51 and ipk <= 4:
	print("=============================================")
	print("|  SELAMAT !!! Anda Lulus Predikat Pujian   |")
	print("=============================================")
elif ipk >= 3.01 and ipk <= 3.5:
	print("=============================================")
	print("|       IPK Anda sangat memuaskan !!!       |")
	print("=============================================")
elif ipk >= 2.76 and ipk <= 3:
	print("=============================================")
	print("|          IPK Anda memuaskan, tok          |")
	print("=============================================")
else:
	print("=============================================")
	print("|         Terus tingkatkan IPK Anda         |")
	print("=============================================")

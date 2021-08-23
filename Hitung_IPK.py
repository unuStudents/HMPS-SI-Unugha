# Python 3.8.6
semester = int(input("Semester berapa? = "))

# Prosedural
total_sks = 0
total_ips = 0
a = 1
while a <= semester:
    print("== Semester Ke-{0} ==".format(a))
    sks = int(input("Masukan Jumlah SKSnya = "))
    ips = float(input("Masukan Nilai IPSnya = "))
    a += 1
    total_sks += sks
    total_ips += ips

ipk = total_ips / semester

# Jawaban
print("\n=========================================")
print("Kamu sudah menempuh {0} semester".format(semester))
print("dan sudah menempuh {0} SKS dari 144 SKS".format(total_sks))
print("IPK kamu : {0:.02f}".format(ipk))
print("=========================================")

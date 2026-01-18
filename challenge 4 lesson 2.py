jam_sekarang = int(input("Jam berapa sekarang:"))
if jam_sekarang < 12:
    print("Selamat Pagi")
elif jam_sekarang <= 17:
    print("Selamat Siang/Sore")
else:
    print("Selamat Malam")

menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print("NIM : 20210801051")
    print("NAMA : REFLY ANDYAZ")
 
    print(" Pilihan")
    print(" 1. capucino")
    print(" 2. es teh ")
    print(" 3. EXIT")
    pilihan = str(input("masukan pilihan"))
    
    if pilihan == "1":
        namaMenu = "capucino"
        harga = int(input("masukan harga ="))
        pajak = 0.1
        harga_final = harga*pajak
        print(harga_final)
    elif pilihan == "2":
        namaMenu = "es teh"
        harga = int(input("masukan harga =   "))
        pajak = 0.1
        harga_final = harga*pajak
        print(harga_final)
    elif pilihan == "3":
        print("terimakasih telah berbelanja")
        exit()
        
   
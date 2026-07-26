# program input
while True:
    # Daftar menu
    print("""
        ░███     ░███                                  
        ░████   ░████                                  
        ░██░██ ░██░██  ░███████  ░████████  ░██    ░██   
        ░██ ░████ ░██ ░██    ░██ ░██    ░██ ░██    ░██ 
        ░██  ░██  ░██ ░█████████ ░██    ░██ ░██    ░██ 
        ░██       ░██ ░██        ░██    ░██ ░██   ░███ 
        ░██       ░██  ░███████  ░██    ░██  ░█████░██ 
                                                    """)
    print(10*"=","Daftar Menu",10*"=")
    print("""
        1. Mie Ayam
        2. Ayam Bakar
        3. Nasi Goreng 
        4. Bakso Mercon
        5. Soto Lamongan
        6. Rawon
            """)
    # proses
    # input menu
    print("\n",10*"=","Menu yang tersedia",10*"=")
    input_Menu = input("Silahkan list menu yang tersedia, [1-6] :")
    # keputusan piihan
    if input_Menu == "1":
        print("\nPilihan : Mie Ayam \nPesanan segera di kirim")
    elif input_Menu == "2":
        print("\nPilihan : Ayam Bakar \nPesanan segera di kirim")
    elif input_Menu == "3":
        print("\nPilihan : Nasi Goreng \nPesanan segera di kirim")
    elif input_Menu == "4":
        print("\nPilihan : Bakso Mercon \nPesanan segera di kirim")
    elif input_Menu == "5":
        print("\nPilihan : Soto Lamongan \nPesanan segera di kirim")
    elif input_Menu == "6":
        print("\nPilihan : Rawon Ponorogo \nPesanan segera di kirim")
    else:
        print("Maaf Menu Tidak tersedia")
        
    # Output 
    # ada pilihan (y/n) untuk melanjutkan program atau tidak
    print(2*"\n",10*"=","Mau lanjut?",10*"=")
    iFlanjut = input("\nMau Pesan lagi (y/n):")
    if iFlanjut == "n":
        print("Terima kasih sudah ke program sederhana ini")
        break # 




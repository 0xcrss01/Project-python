# membuat kalkulator sederhana dengan python 
# serta logika dasar aritmatika 
# berisi penjumlahan, pengurangan, perkalian, pembagian, perpangkatan, modulus, dan keluar dari program

# Calculator Banner
print("""
+-------------------------------------------------------------------------------------------+
|                                                                                           |
|     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗     |
|    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    |
|    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝    |
|    ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗    |
|    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║    |
|     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    |
+-------------------------------------------------------------------------------------------+
    """)

# Kumpulan list operator
OperatorList = ["Penjumlahan (+)","Pengurangan (-)","Perkalian (*)","Pembagian (/)","Perpangkatan (**)","Modulus (%)","Keluar"]


# fungsi dari kumpulan list operator
def listoperator():
    print("\n============================== Program Simple Calculator ==============================\n")
    for index, item in enumerate(OperatorList, start=1): 
        print(f"{index}.{item}")
        
        
# fungsi untuk Program utama 
def main():
    """pengulangan kalkulator jika kondisinya benar (true)"""
    try:
        while True:
            listoperator()
            # input operator
            print("\n=============== Operator ===============")
            operator = int(input("Masukkan operator dan pilih(1,2,..6,7) : ")) # masukkan operator berupa angka

            indeksOperator = operator - 1
            if 0 <= indeksOperator < len(OperatorList):
                listTerpilih = OperatorList[indeksOperator]
                print(f"\nAnda memilih: {listTerpilih}")

            # Program berhenti
            if operator == 7:
                break
            
            # validasi operator
            # nilai range 1-8, kerena angka di dalam bahasa pemrograman dimulai dari 0,
            
            # maka kita buat range atau perkiraan di 1-8 untuk operator keseluruhan yang ada 1-7
            if operator not in range(1, 8):
                print(f"Maaf, {operator} tidak ada dalam operator. Pilih 1-7.")
                continue
            
            # input angka 
            angka1 = float(input("Masukkan Angka1 : ")) # masukkan angka 1
            angka2 = float(input("Masukkan Angka2 : ")) # masukkan angka 2
            
            # jika operator memilih pembagian dan angka 2 adalah nol, 
            # maka akan muncul pesan error dan program akan kembali ke awal untuk memilih operator lagi

            # penanganan khusus untuk pembagian nol
            if operator == 4 and angka2 == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
                continue
            
            ## kondisi dan keputusan yang kita input
            if operator == 1:
                print("\n===== Hasilnya =====")
                result = angka1 + angka2
                print(f"Hasilnya Adalah:{(round(result, 3))}")
            elif operator == 2:
                print("\n===== Hasilnya =====")
                result = angka1 - angka2
                print(f"Hasilnya Adalah:{(round(result, 3))}")
            elif operator == 3:
                print("\n===== Hasilnya =====")
                result = angka1 * angka2
                print(f"Hasilnya Adalah:{(round(result, 3))}")
            elif operator == 4:
                print("\n===== Hasilnya =====")
                result = angka1 / angka2
                print(f"Hasilnya Adalah:{(round(result, 3))}")
            elif operator == 5:
                print("\n===== Hasilnya =====")
                result = angka1 ** angka2
                print(f"Hasilnya Adalah:{(round(result, 3))}")
            elif operator == 6:
                print("\n===== Hasilnya =====")
                result = angka1 % angka2
                print(f"Hasilnya Adalah:{(round(result, 3))}")
            else:
                print(f"Maaf,{operator} tidak ada dalam operator")
            
    except KeyboardInterrupt:
        print("Program berhenti (Ctrl + C).")       
    except ValueError: # memastikan nilai input program benar dan solusi agar program tidak error
        print("Pastikan input benar: operator harus angka 1-7, dan angka harus numerik!")
    finally:
        print("Terima kasih sudah menggunakan program ini ")

# Blok ini hanya berjalan jika file ini dieksekusi secara langsung
# Memanggil fungsi main() untuk menjalankan program utama
if __name__ == "__main__":
    main() 


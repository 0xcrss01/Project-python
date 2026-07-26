# cara membuat data sederhana di python
# program ini berisi fitur create dan read pada saat di buat

## data list pengguna
data_user = []

# tampilkan data
def tampilkan_data():
    """ Untuk menampilkan """

    # Cek dulu apakah data kosong
    if not data_user:
        print("\nData masih kosong!")
        print("\nTotal berapa baris => 0\n")
        return # Langsung keluar dari fungsi agar tidak error
    
    print(f"\n===== Daftar List =====\n")
    for i, item in enumerate(data_user, start=1):
        print(f"{i}. {item}")
        pass

    # Cek Total baris
    total_baris = len(data_user)
    print(f"\nTotal berapa baris => {total_baris}\n")

        # #for i in item: # total tabel
        # print(f"\nTotal berapa baris => {i}\n")
    
        
# tambahkan data
def tambah_data():
    """ Input data user """
    try:
        while True:
            # input user
            nama = str(input(f"\nMasukkan nama :"))
            umur = input("Masukkan umur :")
            kelas = input("Kelas berapa :")

            # Cek informasi semetara
            info1 = f"| {nama} | {umur} | {kelas}"
            data_user.append(info1) 

    # fungsi ini akan jalan jika user tekan shortcut berhenti. contoh: Ctrl + C
    except KeyboardInterrupt:
        print(f"\nProgram telah dihentikan oleh pengguna (Ctrl + C).")
        pass

    # menghitung baris dan informasi
    print(f"\n===== Informasi =====")
    for i, info in enumerate(data_user, start=1):
        print(f"{i}.{info}")

# hapus data 
def hapus_data():
    """" hapus data user  """
    # fungsi menampilkan data 
    tampilkan_data()
    if not data_user: # mendeteksi ada data kosong atau tidak. jika ada maka program tidak dijalankan
        return
    try:
        # pilih mana data yang ingin di hapus
        input_Hapus = int(input("Silahkan Mana yang Ingin di Hapus 1,2,3,... : "))

        index_sistem = input_Hapus - 1
        # melihat kondisi yang di pilih
        if 0 <= index_sistem < len(data_user):
            dihapus = data_user.pop(index_sistem) # fungsi pop() untuk hapus
            print(f"Sukses!! untuk Data {dihapus}, pada baris input ke{input_Hapus} ")
        else:
            print("Gagal!, Input tidak Ditemukan")
    except ValueError:
            print(f"Pilihan harus angka, bukan {pilihan}atau Huruf Dan Jangan Lupa Untuk Memilihnya!") 

# Program utama yang berjalan

print(f"\n========== Data List Sederhana ==========")
print(f"\nPilihan:\n1. Tampilkan Data\n2. Tambah Data\n3. Hapus Baris data\n4. Keluar ")
try:
    while True :  
        print("\n==============================")
        pilihan = int(input("Silakan Pilih Nomor Berapa? : "))
        
        if pilihan == 1:  # tampilkan data
            tampilkan_data()
        elif pilihan == 2: # tambah data
            tambah_data()
        elif pilihan == 3: # hapus data
            hapus_data()
        elif pilihan == 4: # program berhenti
            break
        else:
            print("Pilihan Tidak Ada!!")
        
# fungsi ini akan keluar jika user mengetik perintah shortcut di keyboard
except KeyboardInterrupt:
    print("Program berhenti (Ctrl + C).") 
except ValueError:
    print("Pilihan harus angka, bukan simbol atau Huruf Dan Jangan Lupa Memilihnya!") 



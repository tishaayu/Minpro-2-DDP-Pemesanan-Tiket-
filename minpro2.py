from datetime import datetime
import random
import os

maskapai = [
    "Garuda Indonesia",
    "Lion Air",
    "Sriwijaya Air"
]

rute_penerbangan = [
    "Jakarta - Bali",
    "Surabaya - Jakarta",
    "Balikpapan - Yogyakarta"
]

penumpang = []


akun = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}

def cek_angka(teks):
    teks = teks.strip()
    if teks == "":
        return False
    for karakter in teks:
        if karakter not in "0123456789":
            return False
    return True

def login():
    print("\n======================================")
    print("          LOGIN SISTEM TIKET")
    print("======================================")

    kesempatan = 3

    while kesempatan > 0:
        username = input("Username : ")
        password = input("Password : ")

        if username in akun and akun[username]["password"] == password:
            print("\nLogin berhasil!")
            print("Selamat datang,", username)

            return username, akun[username]["role"]

        else:
            kesempatan -= 1
            print("Username atau password salah.")
            print("Sisa percobaan:", kesempatan)

    print("\nAnda gagal login.")
    return None, None

def lihat_maskapai():
    print("\n======================================")
    print("          DAFTAR MASKAPAI")
    print("======================================")

    for i in range(len(maskapai)):
        print(f"{i + 1}. {maskapai[i]}")

def lihat_rute():
    print("\n======================================")
    print("          RUTE PENERBANGAN")
    print("======================================")

    for i in range(len(rute_penerbangan)):
        print(f"{i + 1}. {rute_penerbangan[i]}")

def pesan_tiket():
    print("\n======================================")
    print("             PESAN TIKET")
    print("======================================")

    while True:
        nama = input("Nama penumpang : ").strip()

        if nama == "":
            print("Nama penumpang tidak boleh kosong.")
        else:
            break

    lihat_rute()

    while True:
        input_rute = input("Pilih nomor rute : ")

        if cek_angka(input_rute):
            pilihan_rute = int(input_rute)

            if 1 <= pilihan_rute <= len(rute_penerbangan):
                rute_dipilih = rute_penerbangan[pilihan_rute - 1]
                break
            else:
                print("Nomor rute tidak tersedia.")
        else:
            print("Input harus berupa angka.")

    lihat_maskapai()

    while True:
        input_maskapai = input("Pilih nomor maskapai : ")

        if cek_angka(input_maskapai):
            pilihan_maskapai = int(input_maskapai)

            if 1 <= pilihan_maskapai <= len(maskapai):
                maskapai_dipilih = maskapai[pilihan_maskapai - 1]
                break
            else:
                print("Nomor maskapai tidak tersedia.")
        else:
            print("Input harus berupa angka.")

    waktu_pesan = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    kode_tiket = "TKT" + str(random.randint(10000, 99999))

    data_baru = {
        "kode_tiket": kode_tiket,
        "nama": nama,
        "rute": rute_dipilih,
        "maskapai": maskapai_dipilih,
        "waktu_pesan": waktu_pesan
    }

    penumpang.append(data_baru)

    print("\nTiket berhasil dipesan.")
    print("Kode Tiket :", kode_tiket)
    print("Nama       :", nama)
    print("Rute       :", rute_dipilih)
    print("Maskapai   :", maskapai_dipilih)
    print("Waktu      :", waktu_pesan)

def lihat_penumpang():
    print("\n======================================")
    print("          DAFTAR PEMESAN")
    print("======================================")

    if len(penumpang) == 0:
        print("Belum ada pemesan.")
        return

    for i in range(len(penumpang)):
        data = penumpang[i]
        print(f"\nData ke-{i + 1}")
        print("Kode Tiket :", data["kode_tiket"])
        print("Nama       :", data["nama"])
        print("Rute       :", data["rute"])
        print("Maskapai   :", data["maskapai"])
        print("Waktu      :", data["waktu_pesan"])

def reschedule_tiket():
    print("\n======================================")
    print("          RESCHEDULE TIKET")
    print("======================================")

    if len(penumpang) == 0:
        print("Belum ada tiket.")
        return

    while True:
        nama_cari = input("Masukkan nama penumpang : ").strip()

        ditemukan = False

        for data in penumpang:
            if data["nama"].lower() == nama_cari.lower():
                ditemukan = True

                print("\nData tiket saat ini:")
                print("Nama     :", data["nama"])
                print("Rute     :", data["rute"])
                print("Maskapai :", data["maskapai"])

                while True:
                    print("\nPilihan reschedule:")
                    print("1. Ganti rute")
                    print("2. Ganti maskapai")

                    pilihan = input("Pilih : ")

                    if pilihan == "1":
                        lihat_rute()

                        while True:
                            input_rute = input("Pilih nomor rute baru : ")

                            if cek_angka(input_rute):
                                pilihan_rute = int(input_rute)

                                if 1 <= pilihan_rute <= len(rute_penerbangan):
                                    data["rute"] = rute_penerbangan[pilihan_rute - 1]
                                    print("Rute berhasil diubah.")
                                    break
                                else:
                                    print("Nomor rute tidak tersedia.")
                            else:
                                print("Input harus berupa angka.")

                        break

                    elif pilihan == "2":
                        lihat_maskapai()

                        while True:
                            input_maskapai = input("Pilih nomor maskapai baru : ")

                            if cek_angka(input_maskapai):
                                pilihan_maskapai = int(input_maskapai)

                                if 1 <= pilihan_maskapai <= len(maskapai):
                                    data["maskapai"] = maskapai[pilihan_maskapai - 1]
                                    print("Maskapai berhasil diubah.")
                                    break
                                else:
                                    print("Nomor maskapai tidak tersedia.")
                            else:
                                print("Input harus berupa angka.")

                        break

                    else:
                        print("Pilihan tidak tersedia.")

                break

        if ditemukan:
            break

        print("Nama penumpang tidak ditemukan.")

def batalkan_tiket():
    print("\n======================================")
    print("          BATALKAN TIKET")
    print("======================================")

    if len(penumpang) == 0:
        print("Belum ada tiket.")
        return

    while True:
        nama_cari = input("Masukkan nama penumpang : ").strip()

        ditemukan = False

        for data in penumpang:
            if data["nama"].lower() == nama_cari.lower():
                ditemukan = True

                while True:
                    konfirmasi = input(
                        "Yakin ingin membatalkan tiket? (ya/tidak): "
                    ).lower()

                    if konfirmasi == "ya":
                        penumpang.remove(data)
                        print("Tiket berhasil dibatalkan.")
                        break

                    elif konfirmasi == "tidak":
                        print("Pembatalan dibatalkan.")
                        break

                    else:
                        print("Pilihan tidak tersedia.")

                break

        if ditemukan:
            break

        print("Nama penumpang tidak ditemukan.")

def tambah_penumpang_admin():
    print("\n======================================")
    print("       TAMBAH DATA PENUMPANG")
    print("======================================")

    while True:
        nama = input("Nama penumpang : ").strip()

        if nama == "":
            print("Nama tidak boleh kosong.")
        else:
            break

    lihat_rute()

    while True:
        input_rute = input("Pilih nomor rute : ")

        if cek_angka(input_rute):
            pilihan_rute = int(input_rute)

            if 1 <= pilihan_rute <= len(rute_penerbangan):
                rute_dipilih = rute_penerbangan[pilihan_rute - 1]
                break
            else:
                print("Nomor rute tidak tersedia.")
        else:
            print("Input harus berupa angka.")

    lihat_maskapai()

    while True:
        input_maskapai = input("Pilih nomor maskapai : ")

        if cek_angka(input_maskapai):
            pilihan_maskapai = int(input_maskapai)

            if 1 <= pilihan_maskapai <= len(maskapai):
                maskapai_dipilih = maskapai[pilihan_maskapai - 1]
                break
            else:
                print("Nomor maskapai tidak tersedia.")
        else:
            print("Input harus berupa angka.")

    waktu_pesan = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    kode_tiket = "TKT" + str(random.randint(10000, 99999))

    data_baru = {
        "kode_tiket": kode_tiket,
        "nama": nama,
        "rute": rute_dipilih,
        "maskapai": maskapai_dipilih,
        "waktu_pesan": waktu_pesan
    }

    penumpang.append(data_baru)

    print("Data penumpang berhasil ditambahkan.")

def ubah_penumpang_admin():
    print("\n======================================")
    print("          UBAH DATA PENUMPANG")
    print("======================================")

    if len(penumpang) == 0:
        print("Belum ada data penumpang.")
        return

    while True:
        nama_cari = input("Masukkan nama penumpang : ").strip()

        ditemukan = False

        for data in penumpang:
            if data["nama"].lower() == nama_cari.lower():
                ditemukan = True

                print("\nData ditemukan.")
                print("Nama     :", data["nama"])
                print("Rute     :", data["rute"])
                print("Maskapai :", data["maskapai"])

                nama_baru = input(
                    "Masukkan nama baru (Enter jika tidak diubah): "
                ).strip()

                if nama_baru != "":
                    data["nama"] = nama_baru

                lihat_rute()

                while True:
                    input_rute = input("Pilih rute baru (0 jika tidak diubah): ")

                    if cek_angka(input_rute):
                        pilihan_rute = int(input_rute)

                        if pilihan_rute == 0:
                            break
                        elif 1 <= pilihan_rute <= len(rute_penerbangan):
                            data["rute"] = rute_penerbangan[pilihan_rute - 1]
                            break
                        else:
                            print("Nomor rute tidak tersedia.")
                    else:
                        print("Input harus berupa angka.")

                lihat_maskapai()

                while True:
                    input_maskapai = input("Pilih maskapai baru (0 jika tidak diubah): ")

                    if cek_angka(input_maskapai):
                        pilihan_maskapai = int(input_maskapai)

                        if pilihan_maskapai == 0:
                            break
                        elif 1 <= pilihan_maskapai <= len(maskapai):
                            data["maskapai"] = maskapai[pilihan_maskapai - 1]
                            break
                        else:
                            print("Nomor maskapai tidak tersedia.")
                    else:
                        print("Input harus berupa angka.")

                print("Data penumpang berhasil diubah.")
                break

        if ditemukan:
            break

        print("Nama penumpang tidak ditemukan.")

def hapus_penumpang_admin():
    print("\n======================================")
    print("          HAPUS DATA PENUMPANG")
    print("======================================")

    if len(penumpang) == 0:
        print("Belum ada data penumpang.")
        return

    while True:
        nama_cari = input("Masukkan nama penumpang : ").strip()

        ditemukan = False

        for data in penumpang:
            if data["nama"].lower() == nama_cari.lower():
                ditemukan = True

                while True:
                    konfirmasi = input(
                        "Yakin ingin menghapus data? (ya/tidak): "
                    ).lower()

                    if konfirmasi == "ya":
                        penumpang.remove(data)
                        print("Data penumpang berhasil dihapus.")
                        break

                    elif konfirmasi == "tidak":
                        print("Penghapusan dibatalkan.")
                        break

                    else:
                        print("Pilihan tidak tersedia.")

                break

        if ditemukan:
            break

        print("Nama penumpang tidak ditemukan.")

def menu_admin():
    while True:

        print("\n======================================")
        print("             MENU ADMIN")
        print("======================================")
        print("1. Lihat maskapai")
        print("2. Lihat rute")
        print("3. Lihat data penumpang")
        print("4. Tambah data penumpang")
        print("5. Ubah data penumpang")
        print("6. Hapus data penumpang")
        print("7. Logout")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            lihat_maskapai()

        elif pilihan == "2":
            lihat_rute()

        elif pilihan == "3":
            lihat_penumpang()

        elif pilihan == "4":
            tambah_penumpang_admin()

        elif pilihan == "5":
            ubah_penumpang_admin()

        elif pilihan == "6":
            hapus_penumpang_admin()

        elif pilihan == "7":
            print("Logout berhasil.")
            print("Terima kasih telah menggunakan program")
            break

        else:
            print("Menu tidak tersedia.")

def menu_user():
    while True:

        print("\n======================================")
        print("              MENU USER")
        print("======================================")
        print("1. Lihat maskapai")
        print("2. Lihat rute")
        print("3. Pesan tiket")
        print("4. Lihat daftar pemesan")
        print("5. Reschedule tiket")
        print("6. Batalkan tiket")
        print("7. Logout")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            lihat_maskapai()

        elif pilihan == "2":
            lihat_rute()

        elif pilihan == "3":
            pesan_tiket()

        elif pilihan == "4":
            lihat_penumpang()

        elif pilihan == "5":
            reschedule_tiket()

        elif pilihan == "6":
            batalkan_tiket()

        elif pilihan == "7":
            print("Logout berhasil.")
            print("\nTerima kasih telah menggunakan program")
            break

        else:
            print("Menu tidak tersedia.")

def main():

    print("======================================")
    print("     SISTEM PEMESANAN TIKET PESAWAT")
    print("======================================")

    while True:

        username, role = login()

        if username is None:
            print("Program selesai.")
            break

        if role == "admin":
            input("\nTekan Enter untuk masuk ke menu admin...")
            os.system("cls")
            menu_admin()
            break

        elif role == "user":
            input("\nTekan Enter untuk masuk ke menu user...")
            os.system("cls")
            menu_user()
            break

        else:
            print("Role tidak dikenali.")


main()
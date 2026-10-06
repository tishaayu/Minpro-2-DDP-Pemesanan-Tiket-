# Minpro-2-DDP-Pemesanan-Tiket-

' Nama : Tisha Ayu Nabilah Lubis '

' NIM : 2609116006 '

Ini adalah program pemesanan tiket pesawat sederhana berbasis Python yang dijalankan lewat terminal (CLI), di mana pengguna bisa login sebagai **admin** untuk mengelola data penumpang (tambah, ubah, hapus) atau sebagai **user** untuk memesan tiket, melihat daftar pemesan, melakukan *reschedule*, dan membatalkan pesanan.

## FLOWCHART ##

<img width="831" height="1058" alt="WhatsApp Image 2026-10-06 at 17 15 22" src="https://github.com/user-attachments/assets/069cfefb-06f2-41fc-90a7-efdab911e05a" />

Disini, alur dimulai dari Start, lalu program menampilkan halaman utama dan meminta input username serta password. Program mengecek apakah akun terdaftar dan password-nya cocok. Jika gagal, kesempatan berkurang dari batas maksimal 3 kali. Jika berhasil login, program mengecek peran pengguna (admin atau user) untuk mengarahkan ke menu utama masing-masing.

<img width="1600" height="1171" alt="WhatsApp Image 2026-10-06 at 17 16 32" src="https://github.com/user-attachments/assets/8b46b8fb-5141-4d8c-b350-4a798e2031ee" />

Disini, alur menunjukkan menu utama untuk admin. Admin dapat memilih menu 1 sampai 3 untuk melihat maskapai, rute, dan data penumpang. Pada menu 4 (tambah data), admin menginput nama, rute, dan maskapai yang langsung divalidasi sebelum disimpan. Menu 5 dan 6 digunakan untuk mengubah dan menghapus data penumpang berdasarkan pencarian nama. Menu 7 digunakan untuk keluar dari sistem.

<img width="1600" height="1274" alt="WhatsApp Image 2026-10-06 at 17 21 30" src="https://github.com/user-attachments/assets/7de5fedc-63fb-4e44-a94c-5542a4259804" />

Disini, alur menunjukkan pilihan menu untuk user. User dapat melihat maskapai, rute, memesan tiket dengan menginput data diri serta pilihan rute/maskapai, melihat tiket yang sudah dipesan, melakukan reschedule (mengubah rute atau maskapai), membatalkan tiket, serta logout dari program.

## KODE ##

<img width="584" height="272" alt="image" src="https://github.com/user-attachments/assets/c0817caf-746e-405d-b7dc-ea3a60eac03e" />

Disini, saya mengimpor modul datetime, random, dan os, lalu membuat variabel list untuk menyimpan daftar maskapai, rute penerbangan, list kosong penumpang, serta dictionary akun untuk data login. Selain itu, saya membuat fungsi cek_angka untuk mengecek apakah input dari user berupa angka secara manual tanpa menggunakan fungsi bawaan seperti .isdigit().

<img width="542" height="206" alt="image" src="https://github.com/user-attachments/assets/bba76037-fad3-48ee-8158-4955b7e825d8" />

Disini, saya membuat fungsi login dengan memberikan kesempatan percobaan sebanyak 3 kali menggunakan perulangan while. Program akan mengecek apakah username dan password yang diinput sesuai dengan data pada dictionary akun. Jika berhasil, program mengembalikan username dan role-nya, sedangkan jika 3 kali gagal, sistem akan membatalkan proses login.

<img width="571" height="287" alt="image" src="https://github.com/user-attachments/assets/ff53e21e-96e6-4bda-882e-8002b50a5d92" />

Disini, saya membuat fungsi pesan_tiket untuk proses transaksi oleh user. User diminta menginput nama penumpang, lalu memilih rute dan maskapai yang langsung divalidasi dengan fungsi cek_angka agar memastikan pilihan yang dimasukkan berupa angka dan tersedia pada daftar. Program secara otomatis membuat kode tiket acak menggunakan random.randint() dan mencatat waktu pemesanan menggunakan datetime.now(), lalu menyimpan seluruh datanya ke dalam list penumpang.

<img width="575" height="284" alt="image" src="https://github.com/user-attachments/assets/1ab3a026-a506-43a6-ae07-69ee0882fabf" />

<img width="595" height="278" alt="image" src="https://github.com/user-attachments/assets/23d4401f-6cee-49da-a49a-15f75865046e" />

Disini, saya membuat fungsi pengelolaan data penumpang khusus untuk role admin. Pada fungsi ubah_penumpang_admin, program mencari data berdasarkan nama penumpang lalu memungkinkan admin memperbarui nama, rute, atau maskapai pilihan. Sedangkan pada fungsi hapus_penumpang_admin, program mencari nama penumpang yang dimaksud lalu menghapus data dictionary tersebut dari list penumpang menggunakan perintah .remove().

## OUTPUT ##

<img width="519" height="140" alt="image" src="https://github.com/user-attachments/assets/8aba8c63-ce31-424a-81ec-cf9c9ea07724" />

<img width="557" height="113" alt="image" src="https://github.com/user-attachments/assets/77cc2142-bc87-4c71-bfed-79f18facd503" />

<img width="577" height="268" alt="image" src="https://github.com/user-attachments/assets/c1f0f790-8528-4b68-82e8-cb6174c9dc3d" />

<img width="554" height="245" alt="Screenshot 2026-10-06 174308" src="https://github.com/user-attachments/assets/553e261e-7fac-4397-8ca2-5265326d838f" />

<img width="500" height="200" alt="Screenshot 2026-10-06 174319" src="https://github.com/user-attachments/assets/6cc7ad44-d35b-4211-a03b-9bf506ee87b1" />

import os, time, getpass, csv

os.system('clear')
profilesh_content = """function mylogin() {
    clear
    read -p "Username: " username
    read -s -p "Password: " password
    echo

    if /usr/bin/python ~/.login.py "$username" "$password"; then
        PS1="user@$username:~$ "
        export PS1
        return 0
    else
        export PS1="user@localhost:~$ "
        return 1
    fi
}
source ~/.bash.sh
mylogin
"""

profilesh_path = ".profile.sh"

try:
    with open(profilesh_path, "r") as file:
        existing_content = file.read()
        if "function mylogin()" in existing_content:
            print(f"File {profilesh_path} sudah ada. Tidak ada tindakan yang diambil.")
            os.system('clear')
        else:
            with open(profilesh_path, "a") as append_file:
                append_file.write(profilesh_content)
            print(f"File {profilesh_path} berhasil diperbarui.")
except FileNotFoundError:
    with open(profilesh_path, "w") as create_file:
        create_file.write(profilesh_content)
    print(f"File {profilesh_path} berhasil dibuat.")
    os.system('clear')

login_content = """import csv
import sys

def login(username, password):
    with open('.db.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Penggunaan: python ~/.login.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    if login(username, password):
        print("Berhasil")
        sys.exit(0)
    else:
        print("Gagal: Username atau password salah.")
        sys.exit(1)
"""

login_path = ".login.py"

try:
    with open(login_path, "r") as file:
        existing_content = file.read()
        if existing_content.strip() == login_content.strip():
            print(f"File {login_path} sudah ada dan berisi konten yang sama.")
            os.system('clear')
        else:
            with open(login_path, "w") as write_file:
                write_file.write(login_content)
            print(f"File {login_path} berhasil diperbarui.")
except FileNotFoundError:
    with open(login_path, "w") as create_file:
        create_file.write(login_content)
    print(f"File {login_path} berhasil dibuat.")
    os.system('clear')
    
import csv
import getpass
import os
import time

class PendaftaranPengguna:
    def __init__(self):
        self.username = input("Username: ")
        self.passwd = getpass.getpass("Password: ")
        self.repasswd = getpass.getpass("Ketik ulang Password: ")
        self.full_name = input("Nama Lengkap: ")
        self.group = input("Grup: ")
        self.number = input("Nomor: ")
        self.phone = input("Telepon Kantor: ")
        self.home_phone = input("Telepon Rumah: ")
        self.other = input("Lainnya: ")

    def apakah_password_cocok(self):
        return self.passwd == self.repasswd and self.passwd != ""
        os.system('clear')

    def tampilkan_info(self):
        print(f"\nusername: {self.username}")
        print(f"\nNama Lengkap: {self.full_name}")
        print(f"Grup: {self.group}")
        print(f"Nomor: {self.number}")
        print(f"Telepon: {self.phone}")
        print(f"Telepon Rumah: {self.home_phone}")
        print(f"Lainnya: {self.other}")

    def konfirmasi_informasi(self):
        konfirmasi = input("Apakah informasi sudah benar? [y/n]: ").lower()
        return konfirmasi == 'y'
    
    def konfirmasi_reinput(self):
        konfirmasi = input("Apakah ingin mengulang tambah user? [y/n]: ").lower()
        return konfirmasi == 'y'

    def simpan_ke_csv(self):
        header = ["Username", "Password", "Nama Lengkap", "Grup", "Nomor", "Telepon", "Telepon Rumah", "Lainnya"]
        data = {
            "Username": self.username,
            "Password": self.passwd,
            "Nama Lengkap": self.full_name,
            "Grup": self.group,
            "Nomor": self.number,
            "Telepon": self.phone,
            "Telepon Rumah": self.home_phone,
            "Lainnya": self.other
        }

        with open(".db.csv", mode='a', newline='') as file:
            penulis = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                penulis.writeheader()
            penulis.writerow(data)

    def reinput(self):
        self.__init__()

pengguna = PendaftaranPengguna()

while True:
    if pengguna.apakah_password_cocok():
        pengguna.tampilkan_info()

        if pengguna.konfirmasi_informasi():
            pengguna.simpan_ke_csv()
            print("")
        else:
            print("Informasi pengguna tidak disimpan.")

        if pengguna.konfirmasi_reinput():
            pengguna.reinput()
            os.system('clear')
        else:
            print("Registrasi selesai.")
            break
    else:
        print("Kata sandi tidak cocok atau kata sandi kosong.")
        time.sleep(0.1)
        os.system('clear')
        pengguna = PendaftaranPengguna()

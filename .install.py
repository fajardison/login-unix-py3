import os, time

bashsh_content = """# .bash.sh

alias me='python ~/.me.py'
alias readme='cat ~/.README.md'
alias adduser='python ~/.adduser.py'
alias login='source ~/.profile.sh'
alias chuser='python ~/.user.py'
alias chpass='python ~/.pass.py'
alias ldata='cat ~/.db.csv'
alias clr='clear'

export PS1="user@localhost:~$ "
"""

bashsh_path = ".bash.sh"

try:
    with open(bashsh_path, "r") as file:
        existing_content = file.read()
        if existing_content.strip() == bashsh_content.strip():
            print(f"File {bashsh_path} sudah ada dan berisi konten yang sama.")
        else:
            with open(bashsh_path, "w") as write_file:
                write_file.write(bashsh_content)
            print(f"File {bashsh_path} berhasil diperbarui.")
except FileNotFoundError:
    with open(bashsh_path, "w") as create_file:
        create_file.write(bashsh_content)
    print(f"File {bashsh_path} berhasil dibuat.")
    
bashrc_content = """# .bashrc

{
    source ~/.profile.sh "$username" "$password"
    if [ $? -eq 0 ]; then
        export PS1="user@$username:~$ "
    else
        export PS1="user@localhost:~$ "
    fi
}
"""

bashrc_path = ".bashrc"

try:
    with open(bashrc_path, "r") as file:
        existing_content = file.read()
        if existing_content.strip() == bashrc_content.strip():
            print(f"File {bashrc_path} sudah ada dan berisi konten yang sama.")
        else:
            with open(bashrc_path, "w") as write_file:
                write_file.write(bashrc_content)
            print(f"File {bashrc_path} berhasil diperbarui.")
except FileNotFoundError:
    with open(bashrc_path, "w") as create_file:
        create_file.write(bashrc_content)
    print(f"File {bashrc_path} berhasil dibuat.")

me_content = """# .me.py
import os
import time

def clear_screen():
    os.system('clear')

def print_with_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()  # Add a newline after the animation

# Clear screen
clear_screen()

# Animasi LOGIN TERMUX
print_with_animation(' ========= LOGIN TERMUX =========')
print_with_animation('      Channel MOBILE POPULER')
print_with_animation('      by Dimas Fajar')
print_with_animation(' ================================')
print()  # Add an extra newline for spacing
print_with_animation('  Jangan lupa SUBSCRIBE ya ;)')
print(' ================================')
"""
me_path = ".me.py"

try:
    with open(me_path, "r") as file:
        existing_content = file.read()
        if existing_content.strip() == me_content.strip():
            print(f"File {me_path} sudah ada dan berisi konten yang sama.")
        else:
            with open(me_path, "w") as write_file:
                write_file.write(me_content)
            print(f"File {me_path} berhasil diperbarui.")
except FileNotFoundError:
    with open(me_path, "w") as create_file:
        create_file.write(me_content)
    print(f"File {me_path} berhasil dibuat.")


db_content = """username,password,full name, group, number, work phone, home phone, other
"""

db_path = ".db.csv"

try:
    with open(db_path, "r") as file:
        existing_content = file.read()
        if existing_content.strip() == db_content.strip():
            print(f"File {db_path} sudah ada dan berisi konten yang sama.")
        else:
            with open(db_path, "w") as write_file:
                write_file.write(db_content)
            print(f"File {db_path} berhasil diperbarui.")
except FileNotFoundError:
    with open(db_path, "w") as create_file:
        create_file.write(db_content)
    print(f"File {db_path} berhasil dibuat.")

def loading_bar(percentage):
    bar_length = 20
    block = int(round(bar_length * percentage))
    progress = "[" + "." * block + " " * (bar_length - block) + "]"
    return f"Unix-Python install (32mb)  {progress} {percentage:.0%}"

def run_loading():
    for i in range(101):
        os.system('clear')
        print(loading_bar(i/100))
        time.sleep(0.1)
    
    time.sleep(1)
    os.system('clear')
    print("Unix-Python install  [" + "."*20 + "] done")
    time.sleep(1)

run_loading()

def loading_installation(percentage):
    print("Unix-Python installed  [" + "."*20 + "] done")
    bar_length = 20
    block = int(round(bar_length * percentage))
    progress = "[" + "." * block + " " * (bar_length - block) + "]"
    return f"Unix-Python installation  {progress} {percentage:.0%}"

def run_loading_installation():
    for i in range(101):
        os.system('clear')
        print(loading_installation(i/100))
    time.sleep(1)
    os.system('clear')
    print("Unix-Python installed  [" + "."*20 + "] done")
    print("Unix-Python installation  [" + "."*20 + "] done")
    time.sleep(1)

run_loading_installation()

def loading_setup(percentage):
    print("Unix-Python installed  [" + "."*20 + "] done")
    print("Unix-Python installation  [" + "."*20 + "] done")
    bar_length = 20
    block = int(round(bar_length * percentage))
    progress = "[" + "#" * block + " " * (bar_length - block) + "]"
    return f"Unix-Python setup  {progress} {percentage:.0%}"

def run_loading_setup():
    for i in range(101):
        os.system('clear')
        print(loading_setup(i/100))
        time.sleep(0.1)

    time.sleep(1)
    
    os.system('clear')
    print("Unix-Python installed  [" + "."*20 + "] done")
    print("Unix-Python installation  [" + "."*20 + "] done")
    print("Unix-Python setup  [" + "#"*20 + "] done")
    time.sleep(1)

run_loading_setup()

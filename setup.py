import os
import shutil

def move_files_one_level_up(folder_path):
    current_path = os.path.abspath(os.path.dirname(__file__))
    source_folder = os.path.join(current_path, folder_path)
    destination_folder = os.path.join(current_path, '..')
    try:
        for filename in os.listdir(source_folder):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)
            shutil.move(source_file, destination_file)

        os.rmdir(source_folder)
        print(" ")
        print(f"Silahkan ketikan 'cd ~' untuk keluar dari folder kemudian ketikan 'source ~/.bash' untuk masuk sebagai administrator")
        print(" ")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        os.system('clear')

move_files_one_level_up('')

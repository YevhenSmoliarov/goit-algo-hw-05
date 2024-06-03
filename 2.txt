import os
import shutil
import sys

def copy_files(source_dir, dest_dir):
    # Перевірка чи існує директорія призначення, якщо ні - створюємо
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Рекурсивне копіювання файлів
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Повний шлях до вихідного файлу
            source_file_path = os.path.join(root, file)
            # Розширення файлу
            file_extension = os.path.splitext(file)[1]
            # Шлях до піддиректорії вихідної директорії
            dest_subdir = os.path.join(dest_dir, file_extension[1:])
            # Перевірка чи існує піддиректорія, якщо ні - створюємо
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)
            # Шлях до вихідного файлу
            dest_file_path = os.path.join(dest_subdir, file)
            try:
                # Копіюємо файл у відповідну піддиректорію
                shutil.copy2(source_file_path, dest_file_path)
                print(f"File '{source_file_path}' copied to '{dest_file_path}'")
            except Exception as e:
                print(f"Error copying file '{source_file_path}': {e}")

def main():
    # Перевірка чи передано правильну кількість аргументів
    if len(sys.argv) < 3:
        print("Usage: python script.py source_dir dest_dir")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    # Виклик функції для копіювання файлів
    copy_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()
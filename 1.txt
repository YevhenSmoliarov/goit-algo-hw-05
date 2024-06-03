import os
import shutil
import sys

def copy_files(source_dir, dest_dir):
    # Перевірка чи існує директорія призначення, якщо ні - створюємо
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Рекурсивне копіювання файлів
    for item in os.listdir(source_dir):
        source_item_path = os.path.join(source_dir, item)
        if os.path.isdir(source_item_path):
            # Якщо це піддиректорія, рекурсивно копіюємо файли з неї
            copy_files(source_item_path, dest_dir)
        else:
            # Повний шлях до вихідного файлу
            source_file_path = source_item_path
            # Розширення файлу
            file_extension = os.path.splitext(item)[1]
            # Шлях до піддиректорії вихідної директорії
            dest_subdir = os.path.join(dest_dir, file_extension[1:] if file_extension else 'no_extension')
            # Перевірка чи існує піддиректорія, якщо ні - створюємо
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)
            # Шлях до вихідного файлу
            dest_file_path = os.path.join(dest_subdir, item)
            try:
                # Копіюємо файл у відповідну піддиректорію
                shutil.copy2(source_file_path, dest_file_path)
                print(f"File '{source_file_path}' copied to '{dest_file_path}'")
            except Exception as e:
                print(f"Error copying file '{source_file_path}': {e}")

def main():
    # Перевірка чи передано правильну кількість аргументів
    if len(sys.argv) < 2:
        print("Usage: python script.py source_dir [dest_dir]")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    # Виклик функції для копіювання файлів
    copy_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()
import os
import asyncio
import shutil

# Автоматичне створення вихідної та цільової папок для тесту
source_folder = "C:/Users/shuri/ComputerSystem_GoIT/goit-cs-hw-05/source_test_auto"
output_folder = "C:/Users/shuri/ComputerSystem_GoIT/goit-cs-hw-05/output_test_auto"

# Автоматичне створення вихідної папки та додавання прикладового файлу
os.makedirs(source_folder, exist_ok=True)

# Створюємо прикладовий файл з використанням кодування UTF-8
example_file_path = os.path.join(source_folder, "example.txt")
with open(example_file_path, "w", encoding="utf-8") as example_file:
    example_file.write("Це автоматично створений тестовий файл.")

# Автоматичне створення цільової папки
os.makedirs(output_folder, exist_ok=True)

# Асинхронна функція для читання вихідної папки та копіювання файлів
async def read_folder(source_folder, output_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            await copy_file(file_path, output_folder)

# Асинхронна функція для копіювання файлів за розширенням у цільову папку
async def copy_file(file_path, output_folder):
    ext = os.path.splitext(file_path)[1][1:]  # Отримуємо розширення файлу
    target_folder = os.path.join(output_folder, ext)

    # Створюємо цільову підпапку на основі розширення файлу
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    target_file_path = os.path.join(target_folder, os.path.basename(file_path))
    
    try:
        # Копіюємо файл у відповідну підпапку
        shutil.copy(file_path, target_file_path)
        print(f"Файл {file_path} скопійовано до {target_folder}.")
    except Exception as e:
        print(f"Помилка при копіюванні файлу {file_path}: {e}")

# Основна функція, що запускає програму
async def main():
    print(f"Початок програми з вихідною папкою: {source_folder} та цільовою папкою: {output_folder}")
    
    # Викликаємо асинхронну функцію для читання та копіювання файлів
    await read_folder(source_folder, output_folder)

# Запуск програми
if __name__ == "__main__":
    # Запуск програми
    asyncio.run(main())

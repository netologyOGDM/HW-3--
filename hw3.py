import os

# Папка, в которой находятся файлы
directory = os.path.join(os.getcwd())

# Указываем конкретные файлы, которые нужно обработать
specific_files = ['1.txt', '2.txt'] 
# Список для хранения информации о файлах
file_info = []

# Считываем содержимое файлов и сохраняем информацию о них
for filename in specific_files:
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):  # Проверяем, существует ли файл
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            file_info.append((filename, line_count, lines))

# Сортируем файлы по количеству строк

def get_line_count(file_tuple):
    return file_tuple[1]

# Сортируем файлы по количеству строк
file_info.sort(key=get_line_count)

# Записываем результат в итоговый файл
with open('result.txt', 'w', encoding='utf-8') as result_file:
    for filename, line_count, lines in file_info:
        result_file.write(f"{filename}\n")
        result_file.write(f"{line_count}\n")
        result_file.writelines(lines)

print("Файлы успешно объединены в result.txt.")
print(file_info)
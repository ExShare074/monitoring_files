# Мониторинг изменений файлов
import os
import time

# Указываем путь к директории, которую будем мониторить
directory = 'C:/Users/User/Documents/GitHub'

# Получаем список файлов в директории
files = os.listdir(directory)


files_timestamps = {file: os.path.getmtime(os.path.join(directory, file)) for file in files}

while True:
    # Проверяем изменения файлов
    for file, timestamp in files_timestamps.items():
        new_timestamp = os.path.getmtime(os.path.join(directory, file))
        if new_timestamp != timestamp:
            print(f'Файл {file} был изменен')
            files_timestamps[file] = new_timestamp


    time.sleep(1)
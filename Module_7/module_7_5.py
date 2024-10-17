import os
import time
for files in os.walk("."):
    for file in files:
        for fil in file:
            filepath = os.path.abspath(fil)
            filetime = os.path.getatime(fil)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(fil)
            parent_dir = os.path.curdir
            print((f'Обнаружен файл: {fil}, Путь: {filepath}, '
                   f'Размер: {filesize} байт, Время изменения: {formatted_time}, '
                   f'Родительская директория: {parent_dir}'))
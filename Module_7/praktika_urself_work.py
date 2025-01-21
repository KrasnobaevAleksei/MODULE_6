# добавить пуект меню, Инфо, где написанно как работать с нашим блокнотом
# и пункт о программе кто написал и т.д.

import tkinter
import os
from tkinter import filedialog
from tkinter import Menu

open_ = open("product.txt", "r")
all_products = open_.read()
all_products2 = open_.read() + all_products
open_.close()

def about():
    a = tkinter.Toplevel()
    a.geometry('200x150')
    a['bg'] = 'grey'
    a.overrideredirect(True)
    tkinter.Label(a, text=all_products2).pack(expand=1)
    a.after(5000, lambda: a.destroy())

def file_select():
    filename = filedialog.askopenfile(initialdir="/", title="Выберите файл",
                                      filetypes=(("Тесктовый файл", "txt"),
                                                 ("Вес файлы", "*")))
    text["text"] = filename.name
    os.startfile(filename.name)

window = tkinter.Tk() # Создаем окно
window.title("Проводник")#Заголовок
window.geometry("350x350")# зразмеры окна
window.configure(bg = "black")# цветзаднего фона
window.resizable(False, False)# неизменяемые размеры окна
text = tkinter.Label(window, text="Файл", height=5, width=55 , background="silver")# текс в окне
text.grid(column=1, row=1)

button_select = tkinter.Button(window, text="Выберите файл", width=20, height=3,
                               background="silver", foreground = "blue",
                               command=file_select)
button_select.grid(column=1, row=2)
info_box = tkinter.Label(text= "привет")
# Добавляем Меню
mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label="Инфо",command=about)
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Новый....")
filemenu.add_separator()
filemenu.add_command(label="Выход")

mainmenu.add_cascade(label="Меню", menu=filemenu)

filemenu2 = Menu(filemenu, tearoff=0)
filemenu2.add_command(label="Открыть")
filemenu2.add_command(label="Сохранить...")
filemenu2.add_command(label="Новый....")
filemenu2.add_command(label="Выход")

filemenu.add_cascade(label="Меню", menu=filemenu2)

window.mainloop() # постоянное обновление окна при запуске
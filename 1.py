'''
Создать оконное приложение для вычисления площади и периметра треугольника
по трем сторонам. Стороны должны вводиться с помощью текстовых полей. Для
вычисления используется кнопка «Вычислить». Предусмотреть выдачу сообщений
об ошибке, если треугольник не существует.
'''

import tkinter as tk
from tkinter import messagebox

def func():
    try:
        side1 = int(side1_entry.get())
        side2 = int(side2_entry.get())
        side3 = int(side3_entry.get())
        if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
            p = side1 + side2 + side3
            s = ((p/2) * ((p/2) - side1) * ((p/2) - side2) * ((p/2) - side3)) ** 0.5
            answer_p["text"] = "Периметр: " + str(p)
            answer_s["text"] = "Площадь: " + str(s)
        else:
            messagebox.showerror("Вычисление площади и периметра", "Треугольника не существует")
    except ValueError:
        messagebox.showerror("Вычисление площади и периметра", "Введите корректные значения!")
        

root=tk.Tk()
root.title("Вычисление площади и периметра")
root.geometry("450x300")

side1_label = tk.Label(root, text = "1 сторона:  ")
side1_entry = tk.Entry(root)
side2_label = tk.Label(root, text = "2 сторона: ")
side2_entry = tk.Entry(root)
side3_label = tk.Label(root, text = "3 сторона: ")
side3_entry = tk.Entry(root)
result = tk.Button(root, text = "Результат", command = func)
answer_p=tk.Label(root)
answer_s=tk.Label(root)

side1_label.grid(row = 0, column = 0)
side1_entry.grid(row = 0, column = 1)
side2_label.grid(row = 1, column = 0)
side2_entry.grid(row = 1, column = 1)
side3_label.grid(row = 2, column = 0)
side3_entry.grid(row = 2, column = 1)
result.grid(row = 3, column = 1)
answer_p.grid(row = 4, column = 1)
answer_s.grid(row = 5, column = 1)

root.mainloop()
'''
Создать два списка для тестирующей программы. В первом списке будут храниться 10
вопросов по географии, во втором – правильные ответы. Написать оконное приложение, 
которое случайным образом выбирает из первого списка 5 вопросов (следить, чтобы они не повторялись!) 
и предлагает ввести ответы. Затем подсчитывается количество верных ответов и выводится в окне в виде метки.
'''

import random
import tkinter as tk
from tkinter import messagebox

def func():
    counter = 0
    answer1 = ans1.get()
    if answer1 == answers[n[0]]:
        counter += 1
            
    answer2 = ans2.get()
    if answer2 == answers[n[1]]:
        counter += 1
            
    answer3 = ans3.get()
    if answer3 == answers[n[2]]:
        counter +=1
            
    answer4 = ans4.get()
    if answer4 == answers[n[3]]:
        counter +=1

    answer5 = ans5.get()
    if answer5 == answers[n[4]]:
        counter += 1
            
    result["text"] = "Ваш результат: " + str(counter)
        
        
root = tk.Tk()
root.title("Викторина по географии")
root.geometry("800x300")

questions = ["В каком море ловят рыбу жители трех частей света?",
            "Какой город очень сердитый?",
            "Какое государство мы носим на голове?",
            "Какой город можно найти в компоте?",
            "Какой город квакает?",
            "Какой город может летать?",
            "Какой город состоит из планеты и дерева?",
            "Какое государство хвастается своей принадлежностью к одежде?",
            "Какой континент не имеет рек?",
            "Какой город в Грузии приятно пить в жаркую погоду?"]

answers = ["Средиземное",
           "Грозный",
           "Панама",
           "Изюм",
           "Москва",
           "Орел",
           "Марсель",
           "Ямайка",
           "Антарктида",
           "Боржоми"]

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = random.sample(nums, 5)

que1 = tk.Label(root, text = "1 вопрос:  " + questions[n[0]])
que1.grid(row = 0, column = 0)

ans1 = tk.Entry(root)
ans1.grid(row = 0, column = 1)

que2 = tk.Label(root, text = "2 вопрос:  " + questions[n[1]])
que2.grid(row = 1, column = 0)

ans2 = tk.Entry(root)
ans2.grid(row = 1, column = 1)

que3 = tk.Label(root, text = "3 вопрос:  " + questions[n[2]])
que3.grid(row = 2, column = 0)

ans3 = tk.Entry(root)
ans3.grid(row = 2, column = 1)

que4 = tk.Label(root, text = "4 вопрос:  " + questions[n[3]])
que4.grid(row = 3, column = 0)

ans4 = tk.Entry(root)
ans4.grid(row = 3, column = 1)

que5 = tk.Label(root, text = "5 вопрос:  " + questions[n[4]])
que5.grid(row = 4, column = 0)

ans5 = tk.Entry(root)
ans5.grid(row = 4, column = 1)

result_button = tk.Button(root, text = "Результат", command = func)
result_button.grid(row = 5, column = 1)

result = tk.Label(root)
result.grid(row = 6, column = 1)


root.mainloop()
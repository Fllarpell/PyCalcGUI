import tkinter
from tkinter import *
import re


root = tkinter.Tk()
root.configure(bg="gray49")
root.geometry('800x600+540+220')

#Заголовок
Label(text="Добро пожаловать в калькулятор\nС багами",
      font=("Comic Sans MS", 24, "bold"),
      bg="gray49",
      fg="gray85").pack(side=TOP)

#поле ввода
entryBox = tkinter.Entry(root, width=27)
entryBox.pack(side=TOP, pady=80)
Label(text='Answer: ', font=("Arial", 24, "bold"), bg="gray49").pack(side=TOP, padx=[0, 20])

#Вычислитель
def get_separate_calculate():
    numbers = '1 2 3 4 5 6 7 8 9 0'
    operators = ['+', '-', '/', '//', ':', '*']
    tmp = entryBox.get()  # Помещаем выражение во временную переменную

    # убирает оператор, сохраняет его, выражение сплитает
    if operators[0] in tmp:
        expressions = tmp.split("+")
        operator = '+'
    elif operators[-1] in tmp:
        expressions = tmp.split("*")
        operator = '*'
    else:
        for k in range(len(operators)):
            if operators[k] in tmp:
                operator = operators[k]
        expressions = re.split("-|:|//|/|-", tmp)

    # переводит str в int
    for k in range(len(expressions)):
        expressions[k] = int(expressions[k])

    # подсчет данных
    match operator:
        case "+":
            Answer = expressions[0] + expressions[1]
        case "-":
            Answer = expressions[0] - expressions[1]
        case "/":
            Answer = expressions[0] / expressions[1]
        case "//":
            Answer = expressions[0] // expressions[1]
        case ":":
            Answer = expressions[0] / expressions[1]
        case "*":
            Answer = expressions[0] * expressions[1]
    Answer = str(Answer)
    Label(text=Answer, font=("Arial", 24, "bold"), bg="gray49").place(x=400, y=340)


"""Нужно придумать как удалить овтет после его получения или как закрепить под Answer на постоянной основе без блокировки окна
"""

Button(text='Calculate',
       font=('Arial', 14, 'bold',),
       bg='gray64',
       width=20,
       height=2,
       command=get_separate_calculate).pack(side=BOTTOM, pady=50)


root.mainloop()
#говно залупа пенис хер
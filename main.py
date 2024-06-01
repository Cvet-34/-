# калькулятор
import tkinter as tk

def get_values():                   # создание функции для подсчета значений
    num1 = int(number1_entery.get())
    num2 = int(number2_entery.get())
    return num1, num2

def insert_values(value):            #создание функции для выведения значений в поле ответ
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1,num2 = get_values() # подсчет значений со знаком "+"
    res = num1+num2
    insert_values(res)

def sub():         # подсчет значений со знаком "-"
    num1,num2 = get_values()
    res = num1-num2
    insert_values(res)

def div():                   # подсчет значений со знаком '/'
    num1,num2 = get_values()
    res = num1/num2
    insert_values(res)

def mul():                  # подсчет значений со знаком '*'
    num1,num2 = get_values()
    res = num1*num2
    insert_values(res)


window = tk.Tk() # из библиотеки tk , верем класс Tk()
window.title('Калькулятор') # оменяли название калькулятора.
window.geometry('350x350') # размер поля
window.resizable(False, False) # отсутствие разтяжки поля
button_add = tk.Button(window, text='+', width=2, height=2, command=add) # чтоб создать кнопку
button_add.place(x=100, y=200) # размещение кнопки
batton_sub = tk.Button(window, text='-', width=2, height=2, command=sub) # чтоб создать кнопку
batton_sub.place(x=150, y=200) # размещение кнопки
batton_mul = tk.Button(window, text='*', width=2, height=2, command=mul) # чтоб создать кнопку
batton_mul.place(x=200, y=200) # размещение кнопки
batton_div = tk.Button(window, text='/', width=2, height=2, command=div)
batton_div.place(x=250, y=200) # размещение кнопки
number1_entery = tk.Entry(window, width=28) # создали строки для заполнения пользователем
number1_entery.place(x=100, y=75)
number2_entery = tk.Entry(window, width = 28) # создали строки для заполнения пользователем
number2_entery.place(x=100, y=100)
answer_entry = tk.Entry(window, width = 28) # создали строки
answer_entry.place(x=120, y=300)
number1 = tk.Label(window, text='Введите первое число: ')
number1.place(x=100, y=50)
number2 = tk.Label(window, text ='Введите второе число: ')
number2.place(x=100, y=125)
answer = tk.Label (window, text='Ответ')
answer.place(x=100, y=275)

window. mainloop()  # цикл обовления информации происходящей на экране

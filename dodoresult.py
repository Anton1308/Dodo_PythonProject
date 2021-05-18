import tkinter as tk
#Модуль для combobox (выпадающий список):
from tkinter import ttk

win = tk.Tk()
# переменная для иконки(фавикона) 2 шага:
photo = tk.PhotoImage(file='pizza.png')
win.iconphoto(False, photo)
# смена цвета основного:
win.config(bg='#ccb9b1')
# название окна:
win.title('Додо-Курьер')
# размеры окна (450x450 -это размеры окна, +1050+150 -это отступ слева и сверху):
win.geometry("560x450+950+100")
# блокировка размеров окна (можно поставить True):
win.resizable(False, False)

# (label_1 -это переменная), текстовая инфа в окне:
label_1 = tk.Label (win, text='Начало аренды авто', justify='center',
                         bg='#8c8484',
                         font=('Arial',13,'bold'),
                         padx=5,            #отступы от текста внутри окна
                         pady=5,            #отступы от текста внутри окна
                    # Рамка вокруг текста
                         relief=tk.RAISED)

label_2 = tk.Label (win, text='Конец аренды авто', bg='#8c8484', justify='center',
                         font=('Arial',13,'bold'),
                         padx=10.5,         #отступы от текста внутри окна
                         pady=5,            #отступы от текста внутри окна
                         relief=tk.RAISED)  #границы поля Label

label_3 = tk.Label (win, text='Количество часов аренды, ч =', bg='#8c8484',
                         font=('Arial',13,'bold'),
                         padx=10.5,         #отступы от текста внутри окна
                         pady=5,            #отступы от текста внутри окна
                         relief=tk.RAISED)  #границы поля Label
label_4 = tk.Label (win, text='Количество выполненых заказов, ед =', bg='#8c8484',
                         font=('Arial',12,'bold'),
                         padx=10.5,         #отступы от текста внутри окна
                         pady=5,            #отступы от текста внутри окна
                         relief=tk.RAISED)  #границы поля Label
label_5 = tk.Label (win, text='Пройденное экипажем расстояние, км =', bg='#8c8484',
                         font=('Arial',12,'bold'),
                         padx=10.5,         #отступы от текста внутри окна
                         pady=5,            #отступы от текста внутри окна
                         relief=tk.RAISED)  #границы поля Label

#нижняя часть путевого листа:
label_6 = tk.Label (win, text='Расчет выплаты за смену:', bg='#ccb9b1',
                         font=('Arial',12,'bold'))

#строка вывода результата часов:
Calc_l3 = tk.Entry (win, font=('Arial',13,'bold'), bd=3, justify='center')
Calc_l3.grid(row=3, column=1, stick='wens', padx='3', pady='3')
Calc_l4 = tk.Entry (win, font=('Arial',13,'bold'), bd=3, justify='center')
Calc_l4.grid(row=4, column=1, stick='wens', padx='3', pady='3')
Calc_l5 = tk.Entry (win, font=('Arial',13,'bold'), bd=3, justify='center')
Calc_l5.grid(row=5, column=1, stick='wens', padx='3', pady='3')

#размещение Лейблев в окне:
label_1.grid(row=1, column=0, stick='wens', padx='2', pady='3')
label_2.grid(row=2, column=0, stick='wens', padx='2', pady='2')
label_3.grid(row=3, column=0, stick='wens', padx='2', pady='2')
label_4.grid(row=4, column=0, stick='wens', padx='2', pady='2')
label_5.grid(row=5, column=0, stick='wens', padx='2', pady='2')
label_6.grid(row=6, column=0, stick='wens', padx='2', pady='2')

#часы на смене:
hours = ('9:00','9:15','9:30','9:45','10:00','10:15','10:30','10:45','11:00','11:15','11:30','11:45','12:00',
         '12:15','12:30','12:45','13:00','13:15','13:30','13:45','14:00','14:15','14:30','14:45',
        '15:00','15:15','15:30','15:45','16:00','16:15','16:30','16:45','17:00','17:15','17:30','17:45',
         '18:00','18:15','18:30','18:45','19:00','19:15','19:30','19:45','20:00','20:15','20:30','20:45',
         '21:00','21:15','21:30','21:45','22:00','22:15','22:30','22:45','23:00','23:15','23:30','23:45',
         '0:00','0:15','0:30','0:45','1:00')
# плохо:
# hours_int = [9-00,9-15,9-30,9-45,10-00,10-15,10-30,10-45]

#переменная_1 для выпадающего списка:
combo_l1 = ttk.Combobox(win, values=hours, justify='center', font=('Arial',13,'bold'))
#отображение начальных значений в списке:
combo_l1.current(0)
#переменная_2 для выпадающего списка:
combo_l2 = ttk.Combobox(win, values=hours, justify='center', font=('Arial',13,'bold'))
combo_l2.current(56)
combo_l1.grid(row=1, column=1, stick='wens', padx='2', pady='2')
combo_l2.grid(row=2, column=1, stick='wens', padx='2', pady='2')

win.mainloop()

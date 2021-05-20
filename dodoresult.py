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
win.title('ПУТЕВОЙ ЛИСТ "ДОДО ПИЦЦА АПРЕЛЕВКА-1"')
# размеры окна (450x450 -это размеры окна, +1050+150 -это отступ слева и сверху):
win.geometry("690x570+440+20")
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
#размещение Лейбла в окне:
label_1.grid(row=0, column=0, stick='wens', padx='2', pady='3')

label_2 = tk.Label (win, text='Конец аренды авто', bg='#8c8484', justify='center',
                         font=('Arial',13,'bold'),
                         padx=10.5,         #отступы от текста внутри окна
                         pady=5,            #отступы от текста внутри окна
                         relief=tk.RAISED)  #границы поля Label
#размещение Лейбла в окне:
label_2.grid(row=1, column=0, stick='wens', padx='2', pady='2')

label_3 = tk.Label (win, text='Количество часов аренды, ч. =', bg='#8c8484',
                         font=('Arial',13,'bold'),
                         padx=10.5,         #отступы от текста внутри окна
                         pady=5,            #отступы от текста внутри окна
                         relief=tk.RAISED)  #границы поля Label
#размещение Лейбла в окне:
label_3.grid(row=2, column=0, stick='wens', padx='2', pady='2')
#строка вывода результата часов:
Calc_l3 = tk.Entry (win, font=('Arial',13,'bold'), bd=3, justify='center')
Calc_l3.grid(row=2, column=1, stick='wens', padx='3', pady='3')

label_4 = tk.Label (win, text='Количество выполненых заказов, ед. =', bg='#8c8484',
                         font=('Arial',12,'bold'),
                         padx=10.5,         #отступы от текста внутри окна
                         pady=5,            #отступы от текста внутри окна
                         relief=tk.RAISED)  #границы поля Label
#размещение Лейбла в окне:
label_4.grid(row=3, column=0, stick='wens', padx='2', pady='2')
#строка вывода результата часов:
Calc_l4 = tk.Entry (win, font=('Arial',13,'bold'), bd=3, justify='center')
Calc_l4.grid(row=3, column=1, stick='wens', padx='3', pady='3')

label_5 = tk.Label (win, text='Пройденное экипажем расстояние, км =', bg='#8c8484',
                         font=('Arial',12,'bold'),
                         padx=10.5,         #отступы от текста внутри окна
                         pady=5,            #отступы от текста внутри окна
                         relief=tk.RAISED)  #границы поля Label
#размещение Лейбла в окне:
label_5.grid(row=4, column=0, stick='wens', padx='2', pady='2')
#строка вывода результата часов:
Calc_l5 = tk.Entry (win, font=('Arial',13,'bold'), bd=3, justify='center')
Calc_l5.grid(row=4, column=1, stick='wens', padx='3', pady='3')

#нижняя часть путевого листа:
label_6 = tk.Label (win, text='Расчет выплаты за смену:', bg='#ccb9b1', font=('Arial',12,'bold'))
label_6.grid(row=5, column=0, stick='wens', padx='2', pady='2')

label_7 = tk.Label (win, text='часов аренды х 96 руб.=', bg='#ccb9b1', font=('Arial',12,'bold'))
label_7.grid(row=6, column=0, stick='e', padx='2', pady='2')
#окно ввода возле 'часов аренды х 96 руб.=':
Calc_l7 = tk.Entry (win, font=('Arial',13,'bold'),width=13, bd=1, justify='center')
Calc_l7.grid(row=6, column=0, stick='w', padx='2', pady='3')
Calc_l77 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l77.grid(row=6, column=1, stick='we', padx='3', pady='3')

label_8 = tk.Label (win, text='заказов (1 сектор) х 64 руб.=', justify='left', bg='#ccb9b1', font=('Arial',11,'bold'))
label_8.grid(row=7, column=0, stick='e', padx='2', pady='2')
#окно ввода возле 'заказов (1й сектор) х 64 руб.=':
Calc_l8 = tk.Entry (win, font=('Arial',13,'bold'),width=13, bd=1, justify='center')
Calc_l8.grid(row=7, column=0, stick='w', padx='3', pady='3')
Calc_l88 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l88.grid(row=7, column=1, stick='we', padx='3', pady='3')

label_9 = tk.Label (win, text='заказов (2 сектор) х 85 руб.=', justify='left', bg='#ccb9b1', font=('Arial',11,'bold'))
label_9.grid(row=8, column=0, stick='e', padx='2', pady='2')
#окно ввода возле 'заказов (2й сектор) х 85 руб.=':
Calc_l9 = tk.Entry (win, font=('Arial',13,'bold'),width=13, bd=1, justify='center')
Calc_l9.grid(row=8, column=0, stick='w', padx='3', pady='3')
Calc_l99 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l99.grid(row=8, column=1, stick='we', padx='3', pady='3')

label_10 = tk.Label (win, text='заказов (3 сектор) х 106 руб.=', justify='left', bg='#ccb9b1', font=('Arial',11,'bold'))
label_10.grid(row=9, column=0, stick='e', padx='2', pady='2')
#окно ввода возле 'заказов (3й сектор) х 106 руб.=':
Calc_l10 = tk.Entry (win, font=('Arial',13,'bold'),width=13, bd=1, justify='center')
Calc_l10.grid(row=9, column=0, stick='w', padx='3', pady='3')
Calc_l1010 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l1010.grid(row=9, column=1, stick='we', padx='3', pady='3')

label_11 = tk.Label (win, text='заказов (4 сектор) х 128 руб.=', justify='left', bg='#ccb9b1', font=('Arial',11,'bold'))
label_11.grid(row=10, column=0, stick='e', padx='2', pady='2')
#окно ввода возле 'заказов (4й сектор) х 128 руб.=':
Calc_l11 = tk.Entry (win, font=('Arial',13,'bold'),width=13, bd=1, justify='center')
Calc_l11.grid(row=10, column=0, stick='w', padx='3', pady='3')
Calc_l1111 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l1111.grid(row=10, column=1, stick='we', padx='3', pady='3')

#заказы1 после 23:00ч:
label_12 = tk.Label (win, text='Заказ после 23:00, руб. = ', bg='#ccb9b1', font=('Arial',11,'bold'))
label_12.grid(row=11, column=0, stick='w', padx='2', pady='2')
#окно1 ввода возле 'Заказы после 23:00':
Calc_l12 = tk.Entry (win, font=('Arial',13,'bold'),width=17, bd=1, justify='center')
Calc_l12.grid(row=11, column=0, stick='e', padx='3', pady='3')
Calc_l1212 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l1212.grid(row=11, column=1, stick='we', padx='3', pady='3')

#заказы2 после 23:00ч:
label_13 = tk.Label (win, text='Заказ после 23:00, руб. = ', bg='#ccb9b1', font=('Arial',11,'bold'))
label_13.grid(row=12, column=0, stick='w', padx='2', pady='2')
#окно2 ввода возле 'Заказы после 23:00':
Calc_l13 = tk.Entry (win, font=('Arial',13,'bold'),width=17, bd=1, justify='center')
Calc_l13.grid(row=12, column=0, stick='e', padx='3', pady='3')
Calc_l1313 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l1313.grid(row=12, column=1, stick='we', padx='3', pady='3')

#расчет километража х 2 руб:
label_14 = tk.Label (win, text='километров х 2 руб. =', justify='left', bg='#ccb9b1', font=('Arial',11,'bold'))
label_14.grid(row=14, column=0, stick='e', padx='2', pady='2')
#окно ввода возле 'километров х 2 руб. =':
Calc_l14 = tk.Entry (win, font=('Arial',13,'bold'),width=19, bd=1, justify='center')
Calc_l14.grid(row=14, column=0, stick='w', padx='3', pady='3')
Calc_l1414 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l1414.grid(row=14, column=1, stick='we', padx='3', pady='3')

#доп.вознаграждение1 :
label_13 = tk.Label (win, text='Доп. вознаграждение, руб. = ', bg='#ccb9b1', font=('Arial',11,'bold'))
label_13.grid(row=15, column=0, stick='w', padx='2', pady='2')
#окно1 ввода возле 'Доп. вознаграждение':
Calc_l13 = tk.Entry (win, font=('Arial',13,'bold'),width=14, bd=1, justify='center')
Calc_l13.grid(row=15, column=0, stick='e', padx='3', pady='3')
Calc_l1313 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l1313.grid(row=15, column=1, stick='we', padx='3', pady='3')

#доп.вознаграждение2 :
label_13 = tk.Label (win, text='Доп. вознаграждение, руб. = ', bg='#ccb9b1', font=('Arial',11,'bold'))
label_13.grid(row=16, column=0, stick='w', padx='2', pady='2')
#окно2 ввода возле 'Доп. вознаграждение':
Calc_l13 = tk.Entry (win, font=('Arial',13,'bold'),width=14, bd=1, justify='center')
Calc_l13.grid(row=16, column=0, stick='e', padx='3', pady='3')
Calc_l1313 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l1313.grid(row=16, column=1, stick='we', padx='3', pady='3')

#итого за день к получению :
label_7 = tk.Label (win, text='Итого за день к получению, включая НПД 6%, руб. :', bg='#ccb9b1', font=('Arial',12,'bold'))
label_7.grid(row=17, column=0, stick='e', padx='2', pady='2')
#окно ввода возле 'Итого за день к получению, включая НПД 6%':
Calc_l7 = tk.Entry (win, font=('Arial',13,'bold'), fg='red', bd=1, justify='center')
Calc_l7.grid(row=17, column=1, stick='we', padx='3', pady='3')

#С расчетом и итоговой суммой согласен :
label_7 = tk.Label (win, text='С расчетом и итоговой суммой согласен, подпись, Ф.И.О. :', bg='#ccb9b1', font=('Arial',12,'bold'))
label_7.grid(row=18, column=0, stick='e', padx='2', pady='2')
#окно ввода возле 'С расчетом и итоговой суммой согласен':
Calc_l7 = tk.Entry (win, font=('Arial',13,'bold'), bd=1, justify='center')
Calc_l7.grid(row=18, column=1, stick='we', padx='3', pady='3')

#часы на смене:
hours = ('9:00','9:15','9:30','9:45','10:00','10:15','10:30','10:45','11:00','11:15','11:30','11:45','12:00',
         '12:15','12:30','12:45','13:00','13:15','13:30','13:45','14:00','14:15','14:30','14:45',
        '15:00','15:15','15:30','15:45','16:00','16:15','16:30','16:45','17:00','17:15','17:30','17:45',
         '18:00','18:15','18:30','18:45','19:00','19:15','19:30','19:45','20:00','20:15','20:30','20:45',
         '21:00','21:15','21:30','21:45','22:00','22:15','22:30','22:45','23:00','23:15','23:30','23:45',
         '0:00','0:15','0:30','0:45','1:00')
#переменная_1 для выпадающего списка:
combo_l1 = ttk.Combobox(win, values=hours, justify='center', font=('Arial',13,'bold'))
#отображение начальных значений в списке:
combo_l1.current(0)
#переменная_2 для выпадающего списка:
combo_l2 = ttk.Combobox(win, values=hours, justify='center', font=('Arial',13,'bold'))
combo_l2.current(56)
combo_l1.grid(row=0, column=1, stick='wens', padx='2', pady='2')
combo_l2.grid(row=1, column=1, stick='wens', padx='2', pady='2')

win.mainloop()

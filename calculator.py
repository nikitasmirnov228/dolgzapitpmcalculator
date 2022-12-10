from tkinter import*

root = Tk()

#########
ent = Entry(width=10, background="yellow", foreground="green", justify=CENTER)
ent2 = Entry(width=10, background="yellow", foreground="green", justify=CENTER)

lab = Label(width=10, bg='green', fg='yellow')
but = Button(text="Сложить",width=20)
but2 = Button(text="Вычесть",width=20)
but3 = Button(text="Разделить",width=20)
but4 = Button(text="Умножить",width=20)
but5 = Button(text="Разделить без остатка",width=20)
but6 = Button(text="Остаток от деления",width=20)


#######

def addition(event):
    s = ent.get()
    if s.isdigit() ==FALSE:
        lab.config(text="ошибка")
    s = ent2.get()
    if s.isdigit() == FALSE:
        lab.config(text="ошибка")
    else:

        s=int(ent.get())
        ss=int(ent2.get())

        sum=s+ss
        lab.config(text=sum)

def subtraction(event):
    s = ent.get()
    if s.isdigit() ==FALSE:
        lab.config(text="ошибка")
    s = ent2.get()
    if s.isdigit() == FALSE:
        lab.config(text="ошибка")
    else:
        s=int(ent.get())
        ss=int(ent2.get())

        sub=s-ss
        lab.config(text=sub)

def division(event):
    s = ent.get()
    if s.isdigit() ==FALSE:
        lab.config(text="ошибка")
    s = ent2.get()
    if s.isdigit() == FALSE:
        lab.config(text="ошибка")
    else:
        s=int(ent.get())
        ss=int(ent2.get())

        div=s/ss
        lab.config(text=div)

def multiplication(event):
    s = ent.get()
    if s.isdigit() ==FALSE:
        lab.config(text="ошибка")
    s = ent2.get()
    if s.isdigit() == FALSE:
        lab.config(text="ошибка")
    else:
        s=int(ent.get())
        ss=int(ent2.get())

        mul=s*ss
        lab.config(text=mul)

def divisionost(event):
    s = ent.get()
    if s.isdigit() ==FALSE:
        lab.config(text="ошибка")
    s = ent2.get()
    if s.isdigit() == FALSE:
        lab.config(text="ошибка")
    else:
        s=int(ent.get())
        ss=int(ent2.get())

        divost=s//ss
        lab.config(text=divost)

def ostdivision(event):
    s = ent.get()
    if s.isdigit() ==FALSE:
        lab.config(text="ошибка")
    s = ent2.get()
    if s.isdigit() == FALSE:
        lab.config(text="ошибка")
    else:
        s=int(ent.get())
        ss=int(ent2.get())

        ostdiv=s%ss
        lab.config(text=ostdiv)

######
ent.pack(side=LEFT, anchor=NW, fill=Y)
ent2.pack(side=RIGHT, anchor=NW, fill=Y)
lab.pack(fill=X)
but.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()

#########

but.bind('<Button-1>', addition)
but2.bind('<Button-1>', subtraction)
but3.bind('<Button-1>', division)
but4.bind('<Button-1>', multiplication)
but5.bind('<Button-1>', divisionost)
but6.bind('<Button-1>', ostdivision)

root.mainloop()

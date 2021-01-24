import datetime

import time

from tkinter import *

screen=Tk()
screen.title('DIGITAL CLOCK')
screen.geometry('500x300')
screen.resizable(0,0)
screen.configure(background='black')
t1=Label(screen,text='Python Digital Clock',font=('Arial',40),fg='olivedrab1',bg='black')
t1.place(x=20,y=0)


def clock():
    t2=time.strftime("%H:%M:%S %p")
    t3=Label(screen,text=t2,font=('ds digital',40,'bold'),fg='light green',bg='black')
    t3.after(200,clock)
    t3.place(x=80,y=190)
    t4=datetime.date.today()
    t5=Label(screen,text=t4.year,font=('ds digital',40,'bold'),fg='light green',bg='black').place(x=80,y=90)
    t6=Label(screen,text=t4.month,font=('ds digital',40,'bold'),fg='light green',bg='black').place(x=240,y=90)
    t7=Label(screen,text=t4.day,font=('ds digital',40,'bold'),fg='light green',bg='black').place(x=305,y=90)
    t8=Label(screen,text='YEAR',font=('ds digital',15,'bold'),fg='olivedrab1',bg='black').place(x=90,y=145)
    t9=Label(screen,text='MONTH',font=('ds digital',15,'bold'),fg='olivedrab1',bg='black').place(x=215,y=145)
    t10=Label(screen,text='DATE',font=('ds digital',15,'bold'),fg='olivedrab1',bg='black').place(x=305,y=145)
    t11=Label(screen,text='HOUR',font=('ds digital',15,'bold'),fg='olivedrab1',bg='black').place(x=80,y=250)
    t12=Label(screen,text='MIN',font=('ds digital',15,'bold'),fg='olivedrab1',bg='black').place(x=165,y=250)
    t13=Label(screen,text='SEC',font=('ds digital',15,'bold'),fg='olivedrab1',bg='black').place(x=235,y=250)

clock()
screen.mainloop()   




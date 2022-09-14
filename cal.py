
from tkinter import *
cal=Tk()
cal.title("maths")
cal.geometry("600x600")
ram=Entry()
ram.pack()
def sandhosh(num):
    first=ram.get() 
    ram.delete(0,END)
    ram.insert(0,str(first)+str(num))
def add():
    first_number=ram.get()
    global old_Value
    old_Value=int(first_number)
    global math
    math="addition"
    ram.delete(0,END)
def substraction():
    first_number=ram.get()
    global old_Value
    old_Value=int(first_number)
    global math
    math="substraction"
    ram.delete(0,END) 
def multyplication():
    first_number=ram.get()
    global old_Value
    old_Value=int(first_number)
    global math
    math="multyplication"
    ram.delete(0,END)
def division():
    first_number=ram.get()
    global old_Value
    old_Value=int(first_number)
    global math
    math="division"
    ram.delete(0,END)
def equal():
    if math=="addition":    
        new_value=ram.get()
        ram.delete(0,END)
        ram.insert(0,int(old_Value)+int(new_value))
    if math=="substraction":
        new_value=ram.get()
        ram.delete(0,END)
        ram.insert(0,int(old_Value)-int(new_value))
    if math=="multyplication":
        new_value=ram.get()
        ram.delete(0,END)
        ram.insert(0,int(old_Value)*int(new_value))
    if math=="division":
        new_value=ram.get()
        ram.delete(0,END)
        ram.insert(0,int(old_Value)//int(new_value))          
h=Button(cal,text='1',command=lambda:sandhosh(1))
h.place(x='20',y='20')
h2=Button(cal,text='2',command=lambda:sandhosh(2))
h2.place(x='40',y='20')
h3=Button(cal,text='3',command=lambda:sandhosh(3))
h3.place(x=60,y=20)
h4=Button(cal,text='4',command=lambda:sandhosh(4))
h4.place(x=20,y=40)
h5=Button(cal,text='5',command=lambda:sandhosh(5))
h5.place(x=40,y=40)
h6=Button(cal,text='6',command=lambda:sandhosh(6))
h6.place(x=60,y=40)
h7=Button(cal,text='7',command=lambda:sandhosh(7))
h7.place(x=20,y=60)
h8=Button(cal,text='8',command=lambda:sandhosh(8))
h8.place(x=40,y=60)
h9=Button(cal,text='9',command=lambda:sandhosh(9))
h9.place(x=60,y=60)
h10=Button(cal,text='0',height=4,width=2,command=lambda:sandhosh(0))
h10.place(x=80,y=20,)
h11=Button(cal,text='+',height=2,width=2,command=add)
h11.place(x=105,y=20)
h12=Button(cal,text='=',height=4,width=2,command=equal)
h12.place(x=155,y=20)
h13=Button(cal,text='-',height=2,width=2,command=substraction)
h13.place(x=105,y=49.5)
h14=Button(cal,text='*',height=2,width=2,command=multyplication)
h14.place(x=130,y=20)
h15=Button(cal,text='/',height=2,width=2,command=division)
h15.place(x=130,y=52)
cal.mainloop()
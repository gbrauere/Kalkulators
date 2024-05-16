from tkinter import *

mansLogs=Tk() #Tk=tkinter
mansLogs.title('Kalkulators')

def btnClick(number):
    current=e.get() #nolasa skaitli
    e.delete(0,END) #nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) #ievieto displeja
    return 0

def btnCommand(command):
    global number
    global num1 #jāiegaumē skaitlis, darbība
    global mathOp #matemātiskais operators (+,-,*,/)
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0

def Vienads():
    num2=int(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def notirit():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

e=Entry(mansLogs,width=18,bd=10,font=("Arial Black",20),justify="right",bg='#b0ebb2') #izveido ievades logu/displeju

btn0=Button(mansLogs,text='0',padx='35',pady='20',bd='5',font=("Lucida Sans Typewriter",10),command=lambda:btnClick(0),bg='#4dd652'
) #izveido pogu
btn1=Button(mansLogs,text='1',padx='35',pady='20',bd='5',font=("Lucida Sans Typewriter",10),command=lambda:btnClick(1),bg='#4dd652'
)
btn2=Button(mansLogs,text='2',padx='35',pady='20',bd='5',font=("Lucida Sans Typewriter",10),command=lambda:btnClick(2),bg='#4dd652'
)
btn3=Button(mansLogs,text='3',padx='35',pady='20',bd='5',font=("Lucida Sans Typewriter",10),command=lambda:btnClick(3),bg='#4dd652'
)
btn4=Button(mansLogs,text='4',padx='35',pady='20',bd='5',font=("Lucida Sans Typewriter",10),command=lambda:btnClick(4),bg='#4dd652'
)
btn5=Button(mansLogs,text='5',padx='35',pady='20',bd='5',font=("Lucida Sans Typewriter",10),command=lambda:btnClick(5),bg='#4dd652'
)
btn6=Button(mansLogs,text='6',padx='35',pady='20',bd='5',font=("Lucida Sans Typewriter",10),command=lambda:btnClick(6),bg='#4dd652'
)
btn7=Button(mansLogs,text='7',padx='35',pady='20',bd='5',font=("Lucida Sans Typewriter",10),command=lambda:btnClick(7),bg='#4dd652'
)
btn8=Button(mansLogs,text='8',padx='35',pady='20',bd='5',font=("Lucida Sans Typewriter",10),command=lambda:btnClick(8),bg='#4dd652'
)
btn9=Button(mansLogs,text='9',padx='35',pady='20',bd='5',font=("Lucida Sans Typewriter",10),command=lambda:btnClick(9),bg='#4dd652'
)

btnSask=Button(mansLogs,text='+',padx='35',pady='20',bd='5',command=lambda:btnCommand('+'),bg='green',font=("Lucida Sans Typewriter",10))
btnAtn=Button(mansLogs,text='-',padx='35',pady='20',bd='5',command=lambda:btnCommand('-'),bg='green',font=("Lucida Sans Typewriter",10))
btnDal=Button(mansLogs,text='/',padx='35',pady='20',bd='5',command=lambda:btnCommand('/'),bg='green',font=("Lucida Sans Typewriter",10))
btnReiz=Button(mansLogs,text='*',padx='35',pady='20',bd='5',command=lambda:btnCommand('*'),bg='green',font=("Lucida Sans Typewriter",10))
btnC=Button(mansLogs,text='C',padx='35',pady='20',bd='5',command=notirit,bg='green',font=("Lucida Sans Typewriter",10))
btnVien=Button(mansLogs,text='=',padx='35',pady='20',bd='5',command=Vienads,bg='green',font=("Lucida Sans Typewriter",10))

e.grid(row=0,column=0,columnspan=4,) #displeja atrašanās vieta

btnSask.grid(row=2,column=3)
btnAtn.grid(row=3,column=3)
btnDal.grid(row=4,column=3)
btnReiz.grid(row=5,column=3)
btnC.grid(row=5,column=1)
btnVien.grid(row=5,column=2)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)

btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)

btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)

btn0.grid(row=5,column=0)

mansLogs.mainloop()
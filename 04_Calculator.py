from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def main():
    global root
    global e
    

#Define Buttons
    button01 = Button(root, text="1", padx = 40, pady = 20, command=lambda: button_click(1))
    button02 = Button(root, text="2", padx = 40, pady = 20, command=lambda: button_click(2))
    button03 = Button(root, text="3", padx = 40, pady = 20, command=lambda: button_click(3))
    button04 = Button(root, text="4", padx = 40, pady = 20, command=lambda: button_click(4))
    button05 = Button(root, text="5", padx = 40, pady = 20, command=lambda: button_click(5))
    button06 = Button(root, text="6", padx = 40, pady = 20, command=lambda: button_click(6))
    button07 = Button(root, text="7", padx = 40, pady = 20, command=lambda: button_click(7))
    button08 = Button(root, text="8", padx = 40, pady = 20, command=lambda: button_click(8))
    button09 = Button(root, text="9", padx = 40, pady = 20, command=lambda: button_click(9))
    button00 = Button(root, text="0", padx = 40, pady = 20, command=lambda: button_click(0))
    buttonAdd = Button(root, text="+", padx = 39, pady = 20, command=button_add)
    buttonSub = Button(root, text="-", padx = 40, pady = 20, command=button_sub)
    buttonMult = Button(root, text="*", padx = 39, pady = 20, command=button_mult)
    buttonDiv = Button(root, text="/", padx = 39, pady = 20, command=button_div)
    buttonEq = Button(root, text="=", padx = 39, pady = 20, command= button_eq)
    buttonClr = Button(root, text="Clear", padx = 30, pady = 20, command=button_clear)

#Putting Buttons On Screen
    button01.grid(row=3, column=0)
    button02.grid(row=3, column=1)
    button03.grid(row=3, column=2)

    button04.grid(row=2, column=0)
    button05.grid(row=2, column=1)
    button06.grid(row=2, column=2)

    button07.grid(row=1, column=0)
    button08.grid(row=1, column=1)
    button09.grid(row=1, column=2)

    button00.grid(row=4, column=1)
    buttonAdd.grid(row=4, column=0)
    buttonSub.grid(row=5, column=0)
    buttonEq.grid(row=5, column=1)
    buttonClr.grid(row=6, column=1)
    buttonMult.grid(row=4, column=2)
    buttonDiv.grid(row=5, column=2)


    root.mainloop()

def button_click(num):
    temp = e.get()
    e.delete(0, END)
    e.insert(0, str(temp) + str(num))

def button_clear():
    e.delete(0, END)

def button_add():
    global math
    global fNum
    math = "add"
    temp = e.get()
    fNum = int(temp)
    e.delete(0, END)

def button_sub():
    global math
    global fNum
    math = "sub"
    temp = e.get()
    fNum = int(temp)
    e.delete(0, END)

def button_mult():
    global math
    global fNum
    math = "mult"
    temp = e.get()
    fNum = int(temp)
    e.delete(0, END)

def button_div():
    global math
    global fNum
    math = "div"
    temp = e.get()
    fNum = int(temp)
    e.delete(0, END)

def button_eq():
    temp = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, fNum + int(temp))
    elif math == "sub":
        e.insert(0, fNum - int(temp))
    elif math == "mult":
        e.insert(0, fNum * int(temp))
    elif math == "div":
        e.insert(0, fNum / int(temp))
        


main()

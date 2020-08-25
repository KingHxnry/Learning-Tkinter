from tkinter import *

root = Tk()

def main():
    global root 


    myButton = Button(root, text="Click Me!", command=myClick)
    myButton2 = Button(root, text="Don't Click Me!", state=DISABLED)
    myButton3 = Button(root, text="Long Button", padx=50)
    myButton4 = Button(root, text="Tall Button", pady = 50)

    myButton.pack()
    myButton2.pack()
    myButton3.pack()
    myButton4.pack()

    root.mainloop()


def myClick():
    myLabel = Label(root, text="Nice.")
    myLabel.pack()

main()

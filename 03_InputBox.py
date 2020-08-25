from tkinter import *

root = Tk()
e = Entry(root, width=25)
e.pack()

def main():
    global root
    global e

    #Default text:
    #e.insert(0, "Enter Your Name: ")
    
    myButton = Button(root, text="Enter Your Name", command=myClick)
    myButton.pack()


    root.mainloop()


def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

main()

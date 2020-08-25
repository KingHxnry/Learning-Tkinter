from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("yessir")
root.iconbitmap('C:/Users/fishe/Pictures/Icon/finger.ico')


my_img = ImageTk.PhotoImage(Image.open('C:/Users/fishe/Pictures/Icon/rocket.png'))
my_label = Label(image=my_img)
my_label.pack()









button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()





root.mainloop()

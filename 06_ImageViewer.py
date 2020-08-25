from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("yessir")
root.iconbitmap('C:/Users/fishe/Pictures/Icon/finger.ico')

def main():
    global root


    my_img1 = ImageTk.PhotoImage(Image.open('C:/Users/fishe/Pictures/DavidGuy.jpg'))
    my_img2 = ImageTk.PhotoImage(Image.open('C:/Users/fishe/Pictures/theriseofskywalker_template_82.jpg'))
    my_img3 = ImageTk.PhotoImage(Image.open('C:/Users/fishe/Pictures/p1w9yvl98jx41.jpg'))
    my_img4 = ImageTk.PhotoImage(Image.open('C:/Users/fishe/Pictures/pl9n69mrwhx41.jpg'))
    my_img5 = ImageTk.PhotoImage(Image.open('C:/Users/fishe/Pictures/128-1288583_a-giving-an-encouraging-thumbs-up-cutouts-thumbs.png'))

    image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]



    my_label = Label(image=my_img)
    my_label.grid(row=0, column=0, columnspan=3)



    button_back = Button(root, text="<<", command = back)
    button_exit = Button(root, text="EXIT", command=root.quit)
    button_forward = Button(root, text=">>", command = lambda: forward(2))

    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()

def back():
    global my_label
    global button_forward
    global button_back







root.mainloop()
main()

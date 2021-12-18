from os import link
from tkinter import *
from PIL import ImageTk


class Calculator:
    root = Tk()
    root.title("Calculator")
    root.geometry("350x600")
     
    image_num_zero = PhotoImage(file = r'images/zero.png')
    image_num_one = PhotoImage(file = r'images/number-1.png')
    image_num_two = PhotoImage(file = r'images/two.png')
    image_num_three = PhotoImage(file = r'images/three.png')
    image_num_four = PhotoImage(file = r'images/four.png')
    image_num_five = PhotoImage(file = r'images/five.png')
    image_num_six = PhotoImage(file = r'images/six.png')
    image_num_seven = PhotoImage(file = r'images/seven.png')
    image_num_eight = PhotoImage(file = r'images/eight.png')
    image_num_nine = PhotoImage(file = r'images/nine.png')
   
    result_label = Label(root,
                         text = "Result will be shown here.",
                         font = ("Bahnschrift 13"),
                         borderwidth = 2)
    
    result_label.pack(padx = 0, pady = 0)
    result_label.place(x = 70, y = 20, width = 350, height = 50)
    
    number_zero = Button(root,
                         image = image_num_zero, 
                         borderwidth = 0)
    number_zero.pack(padx = 0, pady = 0)
    number_zero.place(x = 10, y = 530)
    
    
    number_one = Button(root,
                        image = image_num_one,
                        borderwidth = 0)
    number_one.pack(padx = 0, pady = 0)
    number_one.place(x = 10, y = 460)
    
    number_two = Button(root,
                              image = image_num_two,
                              borderwidth = 0)
    number_two.pack(padx = 0, pady = 0)
    number_two.place(x = 80, y = 460)
    
    number_four = Button(root,
                        image = image_num_four,
                        borderwidth = 0)
    number_four.pack(padx = 0, pady = 0)
    number_four.place(x = 10, y = 390)
     
    def additon():
         pass
     
     
    def substraction():
         pass
     
     
    def multiply():
         pass
     
     
    def divide():
         pass







mainloop()
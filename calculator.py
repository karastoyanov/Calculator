from tkinter import *


class Calculator:
    root = Tk()
    root.title("Calculator")
    root.resizable(0,0)
    root.geometry("300x600")
    
    
    input_text = StringVar() 
     
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
    image_period = PhotoImage(file = r'images/period.png')
    image_equal = PhotoImage(file = r'images/equal.png')
    image_plus = PhotoImage(file = r'images/plus.png')
    image_minus = PhotoImage(file = r'images/minus.png')
    image_slash = PhotoImage(file = r'images/slash.png')
    image_asterisk = PhotoImage(file = r'images/asterisk.png')
   
    input_frame = Frame(root, 
                        width = 320, 
                        height = 200, 
                        bg = "blue",)
    input_frame.pack(side = TOP)
    
    input_field = Entry(input_frame, 
                        font = ('arial', 18, 'bold'),
                        textvariable= input_text,
                        width = 200,
                        bg = "red",
                        justify = RIGHT)
    input_field.pack(ipady = 10)
    
    number_zero = Button(root,
                         image = image_num_zero, 
                         borderwidth = 0,
                         text = '0',
                         command = lambda: buttonClick(0),
                         cursor = "hand2")
    number_zero.pack(padx = 0, pady = 0)
    number_zero.place(x = 10, y = 530)
    
    
    number_one = Button(root,
                        image = image_num_one,
                        borderwidth = 0,
                        text = '1',
                        command = lambda: buttonClick(1),
                        cursor = "hand2")
    number_one.pack(padx = 0, pady = 0)
    number_one.place(x = 10, y = 460)
    
    number_two = Button(root,
                              image = image_num_two,
                              borderwidth = 0,
                              text = '2',
                              command = lambda: buttonClick(2),
                              cursor = "hand2")
    number_two.pack(padx = 0, pady = 0)
    number_two.place(x = 80, y = 460)
    
    number_three = Button(root,
                          image = image_num_three,
                          borderwidth = 0,
                          text = '3',
                          command = lambda: buttonClick(3),
                          cursor = "hand2")
    number_three.pack(padx = 0, pady = 0)
    number_three.place(x = 150, y = 460)
    
    number_four = Button(root,
                        image = image_num_four,
                        borderwidth = 0,
                        text = '4',
                        command = lambda: buttonClick(4),
                        cursor = "hand2")
    number_four.pack(padx = 0, pady = 0)
    number_four.place(x = 10, y = 390)
    
    number_five = Button(root,
                         image = image_num_five,
                         borderwidth = 0,
                         text = '5',
                         command = lambda: buttonClick(5),
                         cursor = "hand2")
    number_five.pack(padx = 0, pady = 0)
    number_five.place(x = 80, y = 390)
    
    number_six = Button(root,
                        image = image_num_six,
                        borderwidth = 0,
                        text = '6',
                        command = lambda: buttonClick(6),
                        cursor = "hand2")
    number_six.pack(padx = 0, pady = 0)
    number_six.place(x = 150, y = 390)
    
    number_seven = Button(root,
                          image = image_num_seven,
                          borderwidth = 0,
                          text = '7',
                          command = lambda: buttonClick(7),
                          cursor = "hand2")
    number_seven.pack(padx = 0, pady = 0)
    number_seven.place(x = 10, y = 320)
    
    number_eight = Button(root,
                          image = image_num_eight,
                          borderwidth = 0,
                          text = '8',
                          command = lambda: buttonClick(8),
                          cursor = "hand2")
    number_eight.pack(padx = 0, pady = 0)
    number_eight.place(x = 80, y = 320)
    
    number_nine = Button(root,
                         image = image_num_nine,
                         borderwidth = 0,
                         text = '9',
                         command = lambda: buttonClick(9),
                         cursor = "hand2")
    number_nine.pack(padx = 0, pady = 0)
    number_nine.place(x = 150, y = 320)
    
    period = Button(root,
                    image = image_period,
                    borderwidth = 0,
                    text = '.',
                    command = lambda: buttonClick("."),
                    cursor = "hand2")
    period.pack(padx = 0, pady = 0)
    period.place(x = 80, y = 530)
    
    equal = Button(root,
                   image = image_equal,
                   borderwidth = 0,
                   text = '=',
                   command = lambda: buttonClick("="),
                   cursor = "hand2")
    equal.pack(padx = 0, pady = 0)
    equal.place(x = 150, y = 530)
    
    plus = Button(root,
                  image = image_plus,
                  borderwidth = 0,
                  text = '+',
                  command = lambda: buttonClick("+"),
                  cursor = "hand2")
    plus.pack(padx = 0, pady = 0)
    plus.place(x = 220, y = 530)
    
    minus = Button(root,
                   image = image_minus,
                   borderwidth = 0,
                   text = '-',
                   command = lambda: buttonClick("-"),
                   cursor = "hand2")
    minus.pack(padx = 0, pady = 0)
    minus.place(x = 220, y = 460)
    
    slash = Button(root,
                   image = image_slash,
                   borderwidth = 0,
                   text = '/',
                   command = lambda: buttonClick("/"),
                   cursor = "hand2")
    slash.pack(padx = 0, pady = 0)
    slash.place(x = 220, y = 320)
    
    asterisk = Button(root,
                      image = image_asterisk,
                      borderwidth = 0,
                      text = '*',
                      command = lambda: buttonClick("*"),
                      cursor = "hand2")
    asterisk.pack(padx = 0, pady = 0)
    asterisk.place(x = 220, y = 390)


  

def buttonClick(item):
     global expression
     expression = expression + str(item)
     input_text.set(expression)
    
def buttonClear(): 
     global expression 
     expression = "" 
     input_text.set("")
     
def buttonEqual():
     global expression
     result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
     input_text.set(result)
     expression = ""
     
     
expression = ""

input_text = StringVar() 


mainloop()
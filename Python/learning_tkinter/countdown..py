# from tkinter import *

# root = Tk()


# def countdown(count):
#     # change text in label      
#     timer['text'] = count
#     if count > 0:
#         # call countdown again after 1000ms (1s)
#         root.after(1000, countdown, count-1)

# timer = Label(root)
# timer.pack()
# # call countdown first time    
# countdown(5)


# # root.after(0, countdown, 5)
# root.mainloop()
import tkinter 
from tkinter import *
  
  
def callback(input): 
      
    if input.isdigit(): 
        print(input) 
        return True
                          
    elif input is "": 
        print(input) 
        return True
  
    else: 
        print(input) 
        return False
                          
root = Tk() 
  
e = Entry(root) 
e.place(x = 50, y = 50) 
reg = root.register(callback) 
  
e.config(validate ="none",  
         validatecommand =(reg, '% P')) 
  
root.mainloop() 
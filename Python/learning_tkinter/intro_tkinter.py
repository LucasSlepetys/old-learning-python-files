from tkinter import *

root = Tk()

#! Creating function to add to a button:
def myClick():
    label = Label(root, text="You clicked me!!")
    label.pack()

#! Making a button:
myButton = Button(root, text="Click me!", command=myClick, fg="red")
myButton.pack()

root.mainloop()
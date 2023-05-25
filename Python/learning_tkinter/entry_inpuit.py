from tkinter import *

root = Tk()

#!Entry text:
#** Things to change on the entry box: (width=50, bg = "blue", fg="white", borderwidth=20)

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")

#! Creating function to add to a button:
def myClick():
    hello = "Hello " + e.get()
    label = Label(root, text=hello)
    label.pack()

#! Making a button:
myButton = Button(root, text="Enter your name", command=myClick, fg="red")
myButton.pack()

root.mainloop()
# from tkinter import *

# root = Tk()

# def callback(event):
#     print ("clicked at", event.x, event.y)

# frame = Frame(root, width=550, height=520)
# #(event, handler)
# frame.bind("<Button-1>", callback)
# frame.pack()

# root.mainloop()
import tkinter as tk

def createNewWindow():
    global newWindow
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()

app = tk.Tk()
buttonExample = tk.Button(app, 
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

buton = tk.Button(newWindow, text="Hello")
buton.pack()

app.mainloop()
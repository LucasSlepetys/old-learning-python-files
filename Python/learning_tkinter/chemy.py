from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x600")
root.configure(bg="white")
root.title("Chemy")

#! Functions:


#! Page:

chemy_photo = PhotoImage(file="chemi.png")
chemy = Label(root, image=chemy_photo)

#! Page layout:

chemy.pack()





root.mainloop()

from tkinter import *
import webbrowser
import json

root2 = Tk()
root2.geometry("500x700")
root2.configure(bg="white")
root2.title("Notes Screen")

#!Dictionary:

notes = {
    "Note": [
    {
    "Topic" : "-",
    "Notes" : "_",
    "Todo" : "_" }
    ]
}

#!Functions:

def insert():
    with open("notes.json", "a") as f:
        for i in notes["Note"]:
            i["Topic"] = str(e_topic.get())
            i["Notes"] = str(e_notes.get())
            i["Todo"] = str(e_todo.get())
            json.dump(notes["Note"], f, indent = 2)
            e_topic.delete(0, END)
            e_notes.delete(0, END)
            e_todo.delete(0, END)



def open_web(event):
    webbrowser.open("https://www.wolframalpha.com/input/?i=", new=2)

#!Page:

label_title = Label(root2, text="Extra Notes:", font=("Helvetica", 50), fg="red")
label_topic = Label(root2, text="Topic:", font=("Helvetica", 30))
label_notes = Label(root2, text="Notes:", font=("Helvetica", 30))
label_todo = Label(root2, text="TODO:", font=("Helvetica", 30))
e_topic = Entry(root2, width=10, borderwidth=2)
e_notes = Entry(root2, width=10, borderwidth=2)
e_todo = Entry(root2, width=10, borderwidth=2)
button_insert = Button(root2, text="Insert", width=10, command=insert, font=("Helvetica", 25), fg="green")
photo_wol = PhotoImage(file="wolfram.png")
photo_wolfram = Label(root2, image=photo_wol, bg="white")

#!Bild
photo_wolfram.bind("<Button-1>", open_web)

#!Page layout:

label_title.pack(pady=30)
label_topic.pack(pady=(0,5))
e_topic.pack(pady=(0,10), ipady=7, ipadx=100)
label_notes.pack(pady=(0,5))
e_notes.pack(pady=(0,10), ipady=7, ipadx=100)
label_todo.pack(pady=(0,5))
e_todo.pack(pady=(0,10), ipady=7, ipadx=100)
button_insert.pack(pady=30, ipady=7, ipadx=50)
photo_wolfram.pack(pady=40)



#! main loop
root2.mainloop()
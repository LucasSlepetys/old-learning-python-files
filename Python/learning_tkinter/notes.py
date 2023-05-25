from tkinter import *
from tkinter import messagebox
from tkinter import Canvas
import webbrowser
import json

#! First page settings:

root = Tk()
root2 = Tk()
top = Toplevel()
top.geometry("550x650")
top.configure(bg="white")
top.title("Notes")
canvas = Canvas(top, width=370, height=10, borderwidth=1, highlightthickness=1, bg="gray")
canvas2 = Canvas(top, width=10, height=115, borderwidth=1, highlightthickness=1, bg="gray")
canvas3 = Canvas(top, width=10, height=115, borderwidth=1, highlightthickness=1, bg="gray")
canvas4 = Canvas(top, width=370, height=10, borderwidth=1, highlightthickness=1, bg="gray")
canvas.pack()



#! Functions

def math_(event):
    global screen_num
    screen_num = 1
    messagebox.showinfo("Math", "Math note:")
    root.deiconify()
    root2.deiconify()
    top.destroy()
    window_math()
    calcula()

def chemy_(event):
    global screen_num
    screen_num = 2
    messagebox.showinfo("Chemy", "Chemy note:")
    root.deiconify()
    top.destroy()
    window_chemy()

def bussi_(event):
    global screen_num
    screen_num = 3
    messagebox.showinfo("Bussi", "Bussi note:")
    root.deiconify()
    top.destroy()
    window_bussi()

def code_(event):
    global screen_num
    screen_num = 4
    messagebox.showinfo("Code", "Code note:")
    root.deiconify()
    top.destroy()
    window_code()
    
#! Designing windows:

def window_math():
    if screen_num == 1:
        #**Extra notes page:
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
                    messagebox.showinfo("Sending...", "Your information has been sent!")

        def insert_2(event):
            with open("notes.json", "a") as f:
                for i in notes["Note"]:
                    i["Topic"] = str(e_topic.get())
                    i["Notes"] = str(e_notes.get())
                    i["Todo"] = str(e_todo.get())
                    json.dump(notes["Note"], f, indent = 2)
                    e_topic.delete(0, END)
                    e_notes.delete(0, END)
                    e_todo.delete(0, END)
                    messagebox.showinfo("Sending...", "Your information has been sent!")



        def open_web():
            messagebox.showinfo("Opening...", "Opening WolframAlpha website:")
            webbrowser.open("https://www.wolframalpha.com/input/?i=", new=2)

        def close_all():
            messagebox.showwarning("Closing...", "Closing all screens:")
            root.destroy()
            root2.destroy()
            top.destroy()
            

        #!Page:

        label_title = Label(root2, text="Extra Notes:", font=("Helvetica", 50), fg="red")
        label_topic = Label(root2, text="Topic:", font=("Helvetica", 30))
        label_notes = Label(root2, text="Notes:", font=("Helvetica", 30))
        label_todo = Label(root2, text="TODO:", font=("Helvetica", 30))
        e_topic = Entry(root2, width=10, borderwidth=2)
        e_notes = Entry(root2, width=10, borderwidth=2)
        e_todo = Entry(root2, width=10, borderwidth=2)
        button_insert = Button(root2, text="Insert", width=10, command=insert, font=("Helvetica", 25), fg="green")
        open_google = Button(root2, text="Open WolframAlpha Pro", width=20, command=open_web, font=("Helvetica", 25), fg="green")
        close_all = Button(root2, text="Close all", width=10, command=close_all, font=("Helvetica", 25), fg="red")
        
        #photo_wol = PhotoImage(file="wolfram.png")
        #photo_wolfram = Label(root2, image=photo_wol, bg="white")

        e_todo.bind("<Return>", insert_2)

        #!Page layout:

        label_title.pack(pady=30)
        label_topic.pack(pady=(0,5))
        e_topic.pack(pady=(0,10), ipady=7, ipadx=100)
        label_notes.pack(pady=(0,5))
        e_notes.pack(pady=(0,10), ipady=7, ipadx=100)
        label_todo.pack(pady=(0,5))
        e_todo.pack(pady=(0,10), ipady=7, ipadx=100)
        button_insert.pack(pady=30, ipady=7, ipadx=50)
        open_google.pack(pady=20, ipady=7, ipadx=50)
        close_all.pack(pady=10, ipady=7, ipadx=30)
        #photo_wolfram.pack(pady=40)



        


        #! /---------------------/---------------------------/----------------------------/------------------------/
def calcula():  
    if screen_num == 1:    
        #**Simple Calculator
        root.title("Simple Calculator")
        #!Entry text:
        #** Things to change on the entry box: (width=50, bg = "blue", fg="white", borderwidth=20, columspan=3)

        e = Entry(root, width=30, borderwidth=4)
        e.grid(row=0, column=0, columnspan=5, padx=8, pady=8)

        #e.insert(0, "Enter your name: ")

        #! Creating function to add to a button:
        def button_click(number):
            current = e.get()
            e.delete(0, END)
            e.insert(0, str(current) + str(number))

        def button_clear():
            e.delete(0, END)

        def button_add():
            first_number = e.get()
            global f_num
            global math
            math = "addition"
            f_num = int(first_number)
            e.delete(0, END)

        def button_equal():
            second_number = e.get()
            e.delete(0, END)

            if math == "addition":
                e.insert(0, f_num + int(second_number))

            if math == "subtraction":
                e.insert(0, f_num - int(second_number))

            if math == "multiplication":
                e.insert(0, f_num * int(second_number))

            if math == "division":
                e.insert(0, f_num / int(second_number))
            

        def button_subtract():
            first_number = e.get()
            global f_num
            global math
            math = "subtraction"
            f_num = int(first_number)
            e.delete(0, END)

        def button_multiply():
            first_number = e.get()
            global f_num
            global math
            math = "multiplication"
            f_num = int(first_number)
            e.delete(0, END)

        def button_divide():
            first_number = e.get()
            global f_num
            global math
            math = "division"
            f_num = int(first_number)
            e.delete(0, END)

        #! Making a button:

        button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
        button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
        button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
        button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
        button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
        button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
        button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
        button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
        button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
        button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
        button_add = Button(root, text="+", padx=40, pady=20, command= button_add)
        button_equal = Button(root, text="=", padx=92, pady=20, command= button_equal)
        button_clear = Button(root, text="Clear", padx=80, pady=20, command= button_clear)

        button_subtract = Button(root, text="-", padx=41, pady=20, command= button_subtract)
        button_multiply = Button(root, text="*", padx=43.5, pady=20, command= button_multiply)
        button_divide = Button(root, text="/", padx=43.5, pady=20, command= button_divide)

        #! put the buttons on the screen:

        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)

        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)

        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)

        button_0.grid(row=4, column=0)
        button_clear.grid(row=4, column=1, columnspan=2)
        button_add.grid(row=5, column=0)
        button_equal.grid(row=5, column=1, columnspan=2)

        button_subtract.grid(row=6, column=0)
        button_multiply.grid(row=6, column=1)
        button_divide.grid(row=6, column=2)

def window_chemy():
    if screen_num == 2:
        pass

def window_bussi():
    if screen_num == 3:
        pass

def window_code():
    if screen_num == 4:
        pass

def exit():
    top.destroy()
    root.destroy()
    root2.destroy()

#! Page content:
label_sub = Label(top, text="Subjects:", font=("Helvetica", 60), width=7)
photo_math = PhotoImage(file="math.png")
math = Label(top, image=photo_math, bg="white")
photo_chemy = PhotoImage(file="chemy.png")
chemy = Label(top, image=photo_chemy, bg="white")
photo_bussi = PhotoImage(file="bussi.png")
bussi = Label(top, image=photo_bussi, bg="white")
photo_code = PhotoImage(file="code.png")
code = Label(top, image=photo_code, bg="white")
button = Button(top, text="Cancel", command=exit, font=("Helvetica", 40), width=10, fg="red")

#! Line:

canvas.grid(padx=(150,0), pady=(50,50))
canvas.place(x=80, y=130)
canvas2.grid(padx=(150,0), pady=(50,50))
canvas2.place(x=80, y=25)
canvas3.grid(padx=(0,150), pady=(50,50))
canvas3.place(x=440, y=25)
canvas4.grid(padx=(150,0), pady=(50,50))
canvas4.place(x=80, y=20)

#! Bind:

math.bind("<Button-1>", math_)
chemy.bind("<Button-1>", chemy_)
bussi.bind("<Button-1>", bussi_)
code.bind("<Button-1>", code_)

#! Page layout:
label_sub.grid(row=0, column=0, pady=40, padx=(100,0), columnspan=2, )
math.grid(row=2, column=0, pady=20, padx=(100,60))
chemy.grid(row=2, column=1, pady=20)
bussi.grid(row=3, column=0, pady=20, padx=(100,60))
code.grid(row=3, column=1, pady=20)
button.grid(row=4, column=0, padx=(100,0), columnspan=2, pady=(40,0))

#root:
root.geometry("295x410")
root.configure(bg="white")
root.title("Main screen")

root2.geometry("500x700")
root2.configure(bg="white")
root2.title("Notes Screen")
root2.withdraw()

root.withdraw()
root.mainloop()

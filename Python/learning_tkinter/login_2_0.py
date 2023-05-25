from tkinter import * 
from tkinter import messagebox

#Main screen settings:

root = Tk()
top = Toplevel()
top.geometry("400x450")
top.configure(bg="white")
top.title("Login screen")
#Funtions for button:

def verify(event):
    if entry_1.get() == "admin" and entry_2.get() == "Lucas2005" or entry_1.get() == "test" and entry_2.get() == "test":
        messagebox.showinfo("Login", "You successfully logged in!")
        root.deiconify()
        top.destroy()
    elif entry_1.get() != "admin" and entry_2.get() != "Lucas2005" or entry_1.get() != "test" and entry_2.get() != "test":
        messagebox.showerror("Error", "User Name or Password does not Match!")
        return

def exit():
    top.destroy()
    root.destroy()

#Page components

photo2 = PhotoImage(file="login.png")
photo = Label(top, image=photo2, bg="white")
label_log = Label(top, text="User Name:", font=("Helvetica", 20))
label_pass = Label(top, text="Password:", font=("Helvetica", 20))
entry_1 = Entry(top)
entry_2 = Entry(top, show="*")
button = Button(top, text="Cancel", command=exit, width=10, height=1, fg="red", font=("Helvetica", 20))
button_2 = Button(top, text="Sign In", command=lambda:verify(""), width=13, height=1, fg="green", font=("Helvetica", 25))

entry_2.bind('<Return>', verify)


#Pade layouts:

photo.pack(pady=15)
label_log.pack(pady=(0,2))
entry_1.pack(pady=(0,20), ipady=4)
label_pass.pack(pady=(0,2))
entry_2.pack(pady=(0,10), ipady=4)
button_2.pack(pady=(20,0), ipadx=8, ipady=6)
button.pack(pady=(30,5), ipadx=2, ipady=2)


#root:
root.geometry("500x500")
root.configure(bg="white")
root.title("Main screen")
root.withdraw()
root.mainloop()
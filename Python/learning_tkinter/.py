from tkinter import *
import json
import tkinter.font as tkFont
from tkinter import messagebox

#Creating dictionary:

register = { Regis
    [
            {
            "name" : "",
            "last_name" : "",
            "email" : "",
            "password" : "",
            "confirm_password" : "",
            }
    ]
}


#Starting project:
root = Tk()
root.geometry("550x520")
root.title("Login/Register")
root.configure(bg="#D3D3D3")

#Font style:

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle2 = tkFont.Font(family="MS Serif", size=15)


#Funtions:
         
def file_append():
    #! Appending info to file.json:
    register["name"] = e_name.get()
    register["last_name"] = e_lastname.get()
    register["email"] = e_email.get()
    register["password"] = e_password.get()
    register["confirm_password"] = e_confpassword.get()
    with open("register.json", "a") as f:
        json.dump(register, f, indent=2)

def restart():
    #! Restarting register page:
    e_name.delete(0, END)
    e_lastname.delete(0, END)
    e_email.delete(0, END)
    e_password.delete(0, END)
    e_confpassword.delete(0, END)    
    messagebox.showinfo("Registering...", "You were successfully registered!")

def check_fill():  
    #! Checking if all boxes were filled:
    if len(e_name.get()) == 0:
        messagebox.showwarning("Error...", '"Name" is required!')
    elif len(e_lastname.get()) == 0:
        messagebox.showwarning("Error...", '"Last Name" is required!')
    elif len(e_email.get()) == 0:
        messagebox.showwarning("Error...", '"Email" is required!')
    elif len(e_password.get()) == 0:
        messagebox.showwarning("Error...", '"Password" is required!')
    elif e_password.get() != e_confpassword.get():
        messagebox.showwarning("Error...", "Password does not match!")
    else:
        file_append()
        restart() 

def sign_in():
    check_fill()

#Creating new login window:

def log_in():
    #!Root_2 settings:
    global root_2
    root_2 = Tk()
    root_2.geometry("450x420")
    root_2.title("Login")
    root_2.configure(bg="#FFFFFF")
    place()
    root_2.mainloop()

def place():
    #!Creating layour:
    l_log = Label(root_2, text="Please Login", font = ("Lucida Grande", 30), bg="#FFFFFF")
    l_email = Label(root_2, text="Email:", font = ("Lucida Grande", 15), bg="#FFFFFF", fg=("Black")).place(x=115, y=132)
    l_password = Label(root_2, text="Password:", font = ("Lucida Grande", 15), bg="#FFFFFF", fg=("Black")).place(x=115, y=213)
    e_email = Entry(root_2, width=25, bg="#f2f1f1")
    e_password = Entry(root_2, width=25, bg="#f2f1f1")
    button = Button(root_2, width=16, text="Login", fg="Green", padx = 13, pady = 8, font = ("MS Serif", 20), command=find_log).place(x=116, y=310)
    #! Positions:
    l_log.grid(row=0, column=1, pady=(40,30), padx=(115,0))
    e_email.grid(row=1, column=1, ipady=7, pady=(40,20), padx=(115,0))
    e_password.grid(row=2, column=1, ipady=7, pady=(20,40), padx=(115,0))       

#TODO This is not working   
def find_log():
    with open("register.json", "r") as f:
        f_content = json.load(f)
        for key, value in f_content.items():
            print(key, ":", value )



            
    

#Create layout:
label = Label(root, text="Register new account", font=fontStyle, bg="#D3D3D3")
l_name = Label(root, text="Name:", font=fontStyle2, bg="#D3D3D3", anchor=W)
l_lastname = Label(root, text="Last Name:", font=fontStyle2, bg="#D3D3D3")
l_email = Label(root, text="Email:", font=fontStyle2, bg="#D3D3D3")
l_password = Label(root, text="Password:", font=fontStyle2, bg="#D3D3D3")
l_confpass = Label(root, text="Confirm Password:", font=fontStyle2, bg="#D3D3D3")
l_login = Label(root, text="Already have an account?", font=fontStyle2, bg="#D3D3D3", fg="#808080")

e_name = Entry(root, width=25)
e_lastname = Entry(root, width=26)
e_email = Entry(root, width=54)
e_password = Entry(root, width=54)
e_confpassword = Entry(root, width=54)
button = Button(root, text="Create Account", fg="green", command=sign_in, width=15, font=fontStyle, padx=12, pady=10)
button_login = Button(root, text="Login", fg="green", command=log_in, width= 15, font=fontStyle, padx=12, pady=10)

#Set layout to possitions:

label.grid(row=0, column=0, padx=15, pady=10)
e_name.grid(row=2, column=0, padx=8, pady=20, ipady=5)
e_lastname.grid(row=2, column=1, padx=1, pady=20, ipady=5)
e_email.grid(row=4, column=0, padx=10, columnspan=3, pady=20, ipady=7)
e_password.grid(row=6, column=0, columnspan=3, pady=20, ipady=7)
e_confpassword.grid(row=8, column=0, columnspan=3, pady=20, ipady=7)
button.grid(pady=10)
button_login.grid(pady=10)

l_name.place(x=12, y=46)
l_lastname.place(x=261, y=46)
l_email.place(x=7, y=125)
l_password.place(x=7, y=206)
l_confpass.place(x=7, y=286)
l_login.place(x=10, y=374)
button.place(x=286, y=400)
button_login.place(x=10, y=400)




root.mainloop()

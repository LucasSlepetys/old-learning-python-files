TODO This is not working, figure out easier way!
    #! Create new window:
    login_window = Toplevel(root)
    #! Window propeties:
    login_window.geometry("350x320")
    login_window.title("Login")
    login_window.configure(bg="#FFFFFF")
    #! Layout:
    l_log = Label(login_window, text="Member Login", font=fontStyle3, bg="#FFFFFF").place(x=82, y=20)
    e_email = Entry(login_window, width=25, x=75, y=100)
    e_password = Entry(login_window, width=25, x=75, y=160)
    #! Positions:
    l_log.place(x=82, y=20)
    e_email.grid(ipady=7, pady=20)
    e_password.grid(ipady=7, pady=20)
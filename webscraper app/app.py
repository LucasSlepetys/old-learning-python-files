import tkinter as tk
from tkinter import filedialog, Text
import os, subprocess, sys

#*****************************************************#
                #! creating main screen + 
            #! list for all apps selected !#
#*****************************************************#

root = tk.Tk()
apps = []

#*****************************************************#
        #! checking if save.txt already exits + 
  #! reading them and removing the blank space out !#
#*****************************************************#

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

#*****************************************************#
        #! function to add apps to frame !#
#*****************************************************#

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
                                        filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps: 
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

#*****************************************************#
    #! function to run all apps selected on frame !#
#*****************************************************#

def runApps():
    #* Check if user is using windows or mac and used correct function to open aplication:
    for app in apps:
        if sys.platform == "win32":
            os.startfile(app)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, app])

#*****************************************************#
    #! creating canvas and frame for main screen !#
#*****************************************************#

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

#*****************************************************#
            #! creating 2 buttons on root !#
#*****************************************************#

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="#263D42",
                    activeforeground="blue", font = ('calibri', 11, 'bold'), command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="#263D42",
                    activeforeground="blue", font = ('calibri', 11, 'bold'), command=runApps)
runApps.pack()

#*****************************************************#
    #! creating label for all previous apps saved !#
#*****************************************************#

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

#*****************************************************#
                #! run main screen !#
#*****************************************************#

root.mainloop()

#*****************************************************#
#! white all apps with a "," in betweeen on 'save.txt !#
#*****************************************************#

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
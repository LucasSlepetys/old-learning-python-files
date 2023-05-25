from tkinter import *
from tkinter import messagebox
import random

#! Global Varivables:
global list_1
global w_1
global list_label
#! -------

#! List of words:
list_1 = ["about","above","add","after","again","air","all","almost","along","also","always","America","an","and","animal","another","answer","any","are","around","as","ask","at","away","back","be","because","been","before","began","begin","being","below","between","big","book","both","boy","but","by","call","came","can","car","carry","change","children","city","close","come","could","country","cut","day","did","different","do","does","don't","down","each","earth","eat","end","enough","even","every","example","eye","face","family","far","father","feet","few","find","first","follow","food","for","form","found","four","from","get","girl","give","go","good","got","great","group","grow","had","hand","hard","has","have","he","head","hear","help","her","here","high","him","his","home","house","how","idea","if","important","in","Indian","into","is","it","its","it's","just","keep","kind","know","land","large","last","later","learn","leave","left","let","letter","life","light","like","line","list","little","live","long","look","made","make","man","many","may","me","mean","men","might","mile","miss","more","most","mother","mountain","move","much","must","my","name","near","need","never","new","next","night","no","not","now","number","of","off","often","oil","old","on","once","one","only","open","or","other","our","out","over","own","page","paper","part","people","picture","place","plant","play","point","put","question","quick","quickly","quite","read","really","right","river","run","said","same","saw","say","school","sea","second","see","seem","sentence","set","she","should","show","side","small","so","some","something","sometimes","song","soon","sound","spell","start","state","still","stop","story","study","such","take","talk","tell","than","that","the","their","them","then","there","these","they","thing","think","this","those","thought","three","through","time","to","together","too","took","tree","try","turn","two","under","until","up","us","use","very","walk","want","was","watch","water","way","we","well","went","were","what","when","where","which","while","white","who","why","will","with","without","word","work","world","would","write","year","you","young","your"]
w_1 = random.choice(list_1)
w_2 = random.choice(list_1)
w_3 = random.choice(list_1)
w_4 = random.choice(list_1)
w_5 = random.choice(list_1)
w_6 = random.choice(list_1)
w_7 = random.choice(list_1)
w_8 = random.choice(list_1)
w_9 = random.choice(list_1)
w_10 = random.choice(list_1)
w_11 = random.choice(list_1)
w_12 = random.choice(list_1)
w_13 = random.choice(list_1)
w_14 = random.choice(list_1)
w_15 = random.choice(list_1)
w_16 = random.choice(list_1)
#! -------

score = 0
wpm_1 = "WPM = "
wpm = 0
TF = "false"
time = "Time left: "
space = 0
not_score = "."


#!Design:

#Settings
root = Tk()
root.geometry("950x520")
root.title("Typing Fast")
root.configure(bg="#FFFFFF")

#!Functions
def check_color(label, word):
    entry = list_input.get()
    if len(entry) == 1:
        if entry ==  " ":
            label.config(bg="blue")
        elif entry != " ":
            label.config(bg="red")
    elif len(entry) == 2:
        if entry ==  " " + (word[0]):
            label.config(bg="blue")
        elif entry != " " + (word[0]):
            label.config(bg="red")
    elif len(entry) == 3:
        if entry ==  " " + (word[0] + word[1]):
            label.config(bg="blue")
        elif entry !=  " " + (word[0] + word[1]):
            label.config(bg="red")
    elif len(entry) == 4:
        if entry ==  " " + (word[0] + word[1] + word[2]):
            label.config(bg="blue")
        elif entry !=  " " + (word[0] + word[1] + word[2]):
            label.config(bg="red")
    elif len(entry) == 5:
        if entry ==  " " + (word[0] + word[1] + word[2] + word[3]):
            label.config(bg="blue")
        elif entry !=  " " + (word[0] + word[1] + word[2] + word[3]):
            label.config(bg="red")
    elif len(entry) == 6:
        if entry ==  " " + (word[0] + word[1] + word[2] + word[3] + word[4]):
            label.config(bg="blue")
        elif entry !=  " " + (word[0] + word[1] + word[2] + word[3] + word[4]):
            label.config(bg="red")
    elif len(entry) == 7:
        if entry ==  " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5]):
            label.config(bg="blue")
        elif entry !=  " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5]):
            label.config(bg="red")
    elif len(entry) == 8:
        if entry ==  " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6]):
            label.config(bg="blue")
        elif entry !=  " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6]):
            label.config(bg="red")
    elif len(entry) == 9:
        if entry ==  " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6] + word[7]):
            label.config(bg="blue")
        elif entry !=  " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6] + word[7]):
            label.config(bg="red")
    elif len(entry) == 10:
        if entry ==  " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6] + word[7] + word[8]):
            label.config(bg="blue")
        elif entry !=  " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6] + word[7] + word[8]):
            label.config(bg="red")
    elif len(entry) == 11:
        if entry ==  " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6] + word[7] + word[8] + word[9]):
            label.config(bg="blue")
        elif entry !=   " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6] + word[7] + word[8] + word[9]):
            label.config(bg="red")
    elif len(entry) == 12:
        if entry ==  " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6] + word[7] + word[8] + word[9]) + word[10]:
            label.config(bg="blue")
        elif entry !=   " " + (word[0] + word[1] + word[2] + word[3] + word[4] + word[5] + word[6] + word[7] + word[8] + word[9] + word[10]):
            label.config(bg="red")

def check(event):
    if TF == "true":
        #* Global variables
        global w_1
        global w_2
        global w_3
        global w_4
        global w_5
        global w_6
        global w_7
        global w_8
        global w_9
        global w_10
        global w_11
        global w_12
        global w_13
        global w_14
        global w_15
        global w_16
        global score
        global space
        global not_score
        #* If else statements to check if word in label is == to word written
        if space == 0:
            if list_input.get() == w_1 or list_input.get() == str(" " + w_1):
                score = score + 1
                space = space + 1
                not_score = "yes"
                list_input.delete(0, END)
            elif (list_input.get() != w_1 or list_input.get() != str(" " + w_1)) and len(list_input.get()) > 1:
                score = score
                space = space + 1
                not_score = "no"
                list_input.delete(0, END)

        elif space == 1:
            if list_input.get() == w_2 or list_input.get() == str(" " + w_2):
                score = score + 1
                space = space + 1
                not_score = "yes"
                list_input.delete(0, END)
            elif (list_input.get() != w_2 or list_input.get() != str(" " + w_2)) and len(list_input.get()) > 1:
                score = score
                space = space + 1
                not_score = "no"
                list_input.delete(0, END)

        elif space == 2:
            if list_input.get() == w_3 or list_input.get() == str(" " + w_3):
                score = score + 1
                space = space + 1
                not_score = "yes"
                list_input.delete(0, END)
            elif (list_input.get() != w_3 or list_input.get() != str(" " + w_3)) and len(list_input.get()) > 1:
                score = score
                space = space + 1
                not_score = "no"
                list_input.delete(0, END)

        elif space == 3:
            if list_input.get() == w_4 or list_input.get() == str(" " + w_4):
                score = score + 1
                space = space + 1
                not_score = "yes"
                list_input.delete(0, END)
            elif (list_input.get() != w_4 or list_input.get() != str(" " + w_4)) and len(list_input.get()) > 1:
                score = score
                space = space + 1
                not_score = "no"
                list_input.delete(0, END)

        elif space == 4:
            if list_input.get() == w_5 or list_input.get() == str(" " + w_5):
                score = score + 1
                space = space + 1
                not_score = "yes"
                list_input.delete(0, END)
            elif (list_input.get() != w_5 or list_input.get() != str(" " + w_5)) and len(list_input.get()) > 1:
                score = score
                space = space + 1
                not_score = "no"
                list_input.delete(0, END)

        elif space == 5:
            if list_input.get() == w_6 or list_input.get() == str(" " + w_6):
                score = score + 1
                space = space + 1
                not_score = "yes"
                list_input.delete(0, END)
            elif (list_input.get() != w_6 or list_input.get() != str(" " + w_6)) and len(list_input.get()) > 1:
                score = score
                space = space + 1
                not_score = "no"
                list_input.delete(0, END)

        elif space == 6:
            if list_input.get() == w_7 or list_input.get() == str(" " + w_7):
                score = score + 1
                space = space + 1
                not_score = "yes"
                list_input.delete(0, END)
            elif (list_input.get() != w_7 or list_input.get() != str(" " + w_7)) and len(list_input.get()) > 1:
                score = score
                space = space + 1
                not_score = "no"
                list_input.delete(0, END)

        elif space == 7:
            if list_input.get() == w_8 or list_input.get() == str(" " + w_8):
                score = score + 1
                not_score = "yes"
                list_input.delete(0, END)
                w_1 = w_9
                w_2 = w_10
                w_3 = w_11
                w_4 = w_12
                w_5 = w_13
                w_6 = w_14
                w_7 = w_15
                w_8 = w_16

                w_9 = random.choice(list_1)
                w_10 = random.choice(list_1)
                w_11 = random.choice(list_1)
                w_12 = random.choice(list_1)
                w_13 = random.choice(list_1)
                w_14 = random.choice(list_1)
                w_15 = random.choice(list_1)
                w_16 = random.choice(list_1)

                l_1.config(text=w_1)
                l_2.config(text=w_2)
                l_3.config(text=w_3)
                l_4.config(text=w_4)
                l_5.config(text=w_5)
                l_6.config(text=w_6)
                l_7.config(text=w_7)
                l_8.config(text=w_8)
                l_9.config(text=w_9)
                l_10.config(text=w_10)
                l_11.config(text=w_11)
                l_12.config(text=w_12)
                l_13.config(text=w_13)
                l_14.config(text=w_14)
                l_15.config(text=w_15)
                l_16.config(text=w_16)


                space = 0
                l_1.config(fg="white")
                l_2.config(fg="white")
                l_3.config(fg="white")
                l_4.config(fg="white")
                l_5.config(fg="white")
                l_6.config(fg="white")
                l_7.config(fg="white")
            elif (list_input.get() != w_1 or list_input.get() != str(" " + w_1)) and len(list_input.get()) > 1:
                score = score
                not_score = "yes"
                list_input.delete(0, END)
                w_1 = w_9
                w_2 = w_10
                w_3 = w_11
                w_4 = w_12
                w_5 = w_13
                w_6 = w_14
                w_7 = w_15
                w_8 = w_16

                w_9 = random.choice(list_1)
                w_10 = random.choice(list_1)
                w_11 = random.choice(list_1)
                w_12 = random.choice(list_1)
                w_13 = random.choice(list_1)
                w_14 = random.choice(list_1)
                w_15 = random.choice(list_1)
                w_16 = random.choice(list_1)

                l_1.config(text=w_1)
                l_2.config(text=w_2)
                l_3.config(text=w_3)
                l_4.config(text=w_4)
                l_5.config(text=w_5)
                l_6.config(text=w_6)
                l_7.config(text=w_7)
                l_8.config(text=w_8)
                l_9.config(text=w_9)
                l_10.config(text=w_10)
                l_11.config(text=w_11)
                l_12.config(text=w_12)
                l_13.config(text=w_13)
                l_14.config(text=w_14)
                l_15.config(text=w_15)
                l_16.config(text=w_16)


                space = 0
                l_1.config(fg="white")
                l_2.config(fg="white")
                l_3.config(fg="white")
                l_4.config(fg="white")
                l_5.config(fg="white")
                l_6.config(fg="white")
                l_7.config(fg="white")



def countdown(count_1):
    global TF
    global count
    global score
    count = count_1
    timer['text'] = str(time) + str(count)
    if count > 0:
        TF = "true"
        root.after(1000, countdown, count-1)
    elif count == 0:
        global wpm
        wpm = score
        wpm_label.config(text=str(wpm_1) + str(wpm))
        wpm_label.grid(row=5, column=0)
        TF = "false"
        score = 0

def run(event):
    global score
    score = 0
    global TF
    global space
    if TF == "false":
        space = 0
        l_1.config(fg="white")
        l_2.config(fg="white")
        l_3.config(fg="white")
        l_4.config(fg="white")
        l_5.config(fg="white")
        l_6.config(fg="white")
        l_7.config(fg="white")
        l_8.config(fg="white")

        l_1.config(bg="black")
        l_2.config(bg="black")
        l_3.config(bg="black")
        l_4.config(bg="black")
        l_5.config(bg="black")
        l_6.config(bg="black")
        l_7.config(bg="black")
        l_7.config(bg="black")
        l_8.config(bg="black")

        list_input.config(bg="#FFFFFF")
        list_input.config(fg="black")
        list_input.delete(0, END)
        list_input.insert(0, " ")
        TF = "go"
        timer.config(text="Time left: 60")
        l_1.config(bg="blue")
    # elif TF == "true":

def run_auto(event):
    global TF
    if TF == "go":
        if len(list_input.get()) > 1:
            countdown(60)
            TF = "true"


def color():
    pass
    global w_1
    global w_2
    global w_3
    global w_4
    global w_5
    global w_6
    global w_7
    global w_8
    global space
    if TF == "true":

        if space == 0:
            check_color(l_1, w_1)
        elif space != 0:
                l_1.config(bg="black")

        if space == 1:
            check_color(l_2, w_2)
            if not_score == "yes":
                l_1.config(fg="green")
            elif not_score == "no":
                l_1.config(fg="red")
        elif space != 0:
                l_2.config(bg="black")

        if space == 2:
            check_color(l_3, w_3)
            if not_score == "yes":
                l_2.config(fg="green")
            elif not_score == "no":
                l_2.config(fg="red")
        elif space != 2:
                l_3.config(bg="black")

        if space == 3:
            check_color(l_4, w_4)
            if not_score == "yes":
                l_3.config(fg="green")
            elif not_score == "no":
                l_3.config(fg="red")
        elif space != 3:
                l_4.config(bg="black")

        if space == 4:
            check_color(l_5, w_5)
            if not_score == "yes":
                l_4.config(fg="green")
            elif not_score == "no":
                l_4.config(fg="red")
        elif space != 4:
                l_5.config(bg="black")

        if space == 5:
            check_color(l_6, w_6)
            if not_score == "yes":
                l_5.config(fg="green")
            elif not_score == "no":
                l_5.config(fg="red")
        elif space != 5:
                l_6.config(bg="black")

        if space == 6:
            check_color(l_7, w_7)
            if not_score == "yes":
                l_6.config(fg="green")
            elif not_score == "no":
                l_6.config(fg="red")
        elif space != 6:
                l_7.config(bg="black")

        if space == 7:
            check_color(l_8, w_8)
            if not_score == "yes":
                l_7.config(fg="green")
            elif not_score == "no":
                l_7.config(fg="red")
        elif space != 7:
                l_8.config(bg="black")

    if TF == "false":
        if len(list_input.get()) > 0:
            list_input.config(fg="#ff0000")
            list_input.config(bg="#ffff00")





def exit():
    print(score)
    print(not_score)
    root.destroy()

def delete():
    if len(list_input.get()) == 0:
        list_input.insert(0, " ")
    if list_input.get() == "  ":
        list_input.delete(0, END)
        list_input.insert(0, " ")

def both(event):
    delete()
    color()



#! Star Page:
info = Label(root, text="Press 'Enter' to start timer:")
#! Packing:


#! Config of page
Frame(height = 80,width = 660,bg = "black").grid(row=1, column=0, pady=(50,0), padx=(200,150))
timer = Label(root, text="Time left: (press enter)")

#* All labels: -----------------

l_1 = Label(root, text=w_1,bg = "black", fg="white")
l_2 = Label(root, text=w_2,bg = "black", fg="white")
l_3 = Label(root, text=w_3,bg = "black", fg="white")
l_4 = Label(root, text=w_4,bg = "black", fg="white")
l_5 = Label(root, text=w_5,bg = "black", fg="white")
l_6 = Label(root, text=w_6,bg = "black", fg="white")
l_7 = Label(root, text=w_7,bg = "black", fg="white")
l_8 = Label(root, text=w_8,bg = "black", fg="white")
l_9 = Label(root, text=w_9,bg = "black", fg="white")
l_10 = Label(root, text=w_10,bg = "black", fg="white")
l_11 = Label(root, text=w_11,bg = "black", fg="white")
l_12 = Label(root, text=w_12,bg = "black", fg="white")
l_13 = Label(root, text=w_13,bg = "black", fg="white")
l_14 = Label(root, text=w_14,bg = "black", fg="white")
l_15 = Label(root, text=w_15,bg = "black", fg="white")
l_16 = Label(root, text=w_16,bg = "black", fg="white")

#* Finish labels ------------------

list_input = Entry(root)
cancel = Button(root, text="Cancel", command=exit)
wpm_label = Label(root, text=str(wpm_1) + str(wpm))

#! Packing:
info.grid(row=0, column=0, pady=10, padx=150)

#! Grid labels at the top
l_1.grid(row=1, column=0, padx=(0,450), pady=0)
l_2.grid(row=1, column=0, padx=(0,350), pady=0)
l_3.grid(row=1, column=0, padx=(0,250), pady=0)
l_4.grid(row=1, column=0, padx=(0,150), pady=0)
l_5.grid(row=1, column=0, padx=(0,50), pady=0)
l_6.grid(row=1, column=0, padx=(50,0), pady=0)
l_7.grid(row=1, column=0, padx=(150,0), pady=0)
l_8.grid(row=1, column=0, padx=(250,0), pady=0)

#! Grid labels at the bottom
l_9.grid(row=1, column=0, padx=(0,450), pady=(50,0))
l_10.grid(row=1, column=0, padx=(0,350), pady=(50,0))
l_11.grid(row=1, column=0, padx=(0,250), pady=(50,0))
l_12.grid(row=1, column=0, padx=(0,150), pady=(50,0))
l_13.grid(row=1, column=0, padx=(0,50), pady=(50,0))
l_14.grid(row=1, column=0, padx=(50,0), pady=(50,0))
l_15.grid(row=1, column=0, padx=(150,0), pady=(50,0))
l_16.grid(row=1, column=0, padx=(250,0), pady=(50,0))

#! Grid other labels and input areas
list_input.grid(row=2, column=0, pady=1, padx=150)
cancel.grid(row=3, column=0, pady=5, padx=150)
timer.grid(row=4, column=0, pady=10, padx=150)
wpm_label.grid(row=5, column=0, pady=5, padx=150)

#! Bind function
list_input.bind("<space>", check)
root.bind("<Return>", run)

# root.bind("<Key>", color)
# root.bind("<Key>", delete)
root.bind("<Key>", both)

list_input.bind("<Key>", run_auto)








root.mainloop()

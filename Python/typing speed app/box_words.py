from tkinter import *
import random 
import time

root = Tk()
root.geometry("820x520")
root.title("Typing Fast")
root.configure(bg="#FFFFFF")

list_1 = ["about","above","add","after","again","air","all","almost","along","also","always","America","an","and","animal","another","answer","any","are","around","as","ask","at","away","back","be","because","been","before","began","begin","being","below","between","big","book","both","boy","but","by","call","came","can","car","carry","change","children","city","close","come","could","country","cut","day","did","different","do","does","don't","down","each","earth","eat","end","enough","even","every","example","eye","face","family","far","father","feet","few","find","first","follow","food","for","form","found","four","from","get","girl","give","go","good","got","great","group","grow","had","hand","hard","has","have","he","head","hear","help","her","here","high","him","his","home","house","how","idea","if","important","in","Indian","into","is","it","its","it's","just","keep","kind","know","land","large","last","later","learn","leave","left","let","letter","life","light","like","line","list","little","live","long","look","made","make","man","many","may","me","mean","men","might","mile","miss","more","most","mother","mountain","move","much","must","my","name","near","need","never","new","next","night","no","not","now","number","of","off","often","oil","old","on","once","one","only","open","or","other","our","out","over","own","page","paper","part","people","picture","place","plant","play","point","put","question","quick","quickly","quite","read","really","right","river","run","said","same","saw","say","school","sea","second","see","seem","sentence","set","she","should","show","side","small","so","some","something","sometimes","song","soon","sound","spell","start","state","still","stop","story","study","such","take","talk","tell","than","that","the","their","them","then","there","these","they","thing","think","this","those","thought","three","through","time","to","together","too","took","tree","try","turn","two","under","until","up","us","use","very","walk","want","was","watch","water","way","we","well","went","were","what","when","where","which","while","white","who","why","will","with","without","word","work","world","would","write","year","you","young","your"]
w_1 = random.choice(list_1)
w_2 = random.choice(list_1)
w_3 = random.choice(list_1)
w_4 = random.choice(list_1)
w_5 = random.choice(list_1)
w_6 = random.choice(list_1)
space = 0
score = 0
letter = 0



def check(event): 
        global w_1
        global w_2
        global w_3
        global w_4
        global w_5
        global w_6
        global score
        global space
        if space == 0:
            if e_1.get() == w_1 or e_1.get() == str(" " + w_1):
                score = score + 1
                space = space + 1
                e_1.delete(0, END)
        elif space == 1:
            if e_1.get() == w_2 or e_1.get() == str(" " + w_2):
                score = score + 1
                space = space + 1
                e_1.delete(0, END)
        elif space == 2:
            if e_1.get() == w_3 or e_1.get() == str(" " + w_3):
                score = score + 1
                space = space + 1
                e_1.delete(0, END)
                w_1 = w_4
                w_2 = w_5
                w_3 = w_6
                w_4 = random.choice(list_1)
                w_5 = random.choice(list_1)
                w_6 = random.choice(list_1)
                l_1.config(text=w_1)
                l_2.config(text=w_2)
                l_3.config(text=w_3)
                l_4.config(text=w_4)
                l_5.config(text=w_5)
                l_6.config(text=w_6)
                space = 0
        
def check_color(label, word):
    entry = e_1.get()
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




def color_red(event):
    global w_1
    global w_2
    global w_3
    global w_4
    global w_5
    global w_6
    global space
    global letter
    if space == 0:
        w_1_l = e_1.get()
        if len(w_1_l) == 1:
            if w_1_l == (w_1[0]) or w_1_l == " " + (w_1[0]):
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0]) or w_1_l == " " + (w_1[0]):
                l_1.config(bg="red")
        elif len(w_1_l) == 2:
            if w_1_l == (w_1[0] + w_1[1]) or w_1_l == " " + (w_1[0] + w_1[1]):
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0] + w_1[1]) or w_1_l ==  " " + (w_1[0] + w_1[1]):
                l_1.config(bg="red")
        elif len(w_1_l) == 3:
            if w_1_l == (w_1[0] + w_1[1] + w_1[2]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2]):
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0] + w_1[1] + w_1[2]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2]):
                l_1.config(bg="red")
        elif len(w_1_l) == 4:
            if w_1_l == (w_1[0] + w_1[1] + w_1[2] + w_1[3]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3]):
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0] + w_1[1] + w_1[2] + w_1[3]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3]):
                l_1.config(bg="red")
        elif len(w_1_l) == 5:
            if w_1_l == (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4]):
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4]):
                l_1.config(bg="red")
        elif len(w_1_l) == 6:
            if w_1_l == (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5]):
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5]):
                l_1.config(bg="red")
        elif len(w_1_l) == 7:
            if w_1_l == (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6]):
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6]):
                l_1.config(bg="red")
        elif len(w_1_l) == 8:
            if w_1_l == (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7]):
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7]) or " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7]):
                l_1.config(bg="red")
        elif len(w_1_l) == 9:
            if w_1_l == (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8]):
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8]):
                l_1.config(bg="red")
        elif len(w_1_l) == 10:
            if w_1_l == (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8] + w_1[9]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8] + w_1[9]):
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8] + w_1[9]) or w_1_l ==   " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8] + w_1[9]):
                l_1.config(bg="red")
        elif len(w_1_l) == 11:
            if w_1_l == (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8] + w_1[9] + w_1[10]) or w_1_l ==  " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8] + w_1[9]) + w_1[10]:
                l_1.config(bg="blue")
            elif w_1_l != (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8] + w_1[9] + w_1[10]) or w_1_l ==   " " + (w_1[0] + w_1[1] + w_1[2] + w_1[3] + w_1[4] + w_1[5] + w_1[6] + w_1[7] + w_1[8] + w_1[9] + w_1[10]):
                l_1.config(bg="red")
    if space == 1:
        check_color(l_2, w_2)
    
    
    

        
      

        

    
        
Frame(height = 80,width = 660,bg = "black").grid(row=1, column=0, pady=(50,0), padx=(200,150))
l_1 = Label(root, text=w_1,bg = "black", fg="white")
l_1.grid(row=1, column=0, padx=(0,450), pady=0)
l_2 = Label(root, text=w_2,bg = "black", fg="white")
l_2.grid(row=1, column=0, padx=(0,350), pady=0)
l_3 = Label(root, text=w_3,bg = "black", fg="white")
l_3.grid(row=1, column=0, padx=(0,250), pady=0)


l_4 = Label(root, text=w_4,bg = "black", fg="white")
l_4.grid(row=1, column=0, padx=(0,450), pady=(50,0))
l_5 = Label(root, text=w_5,bg = "black", fg="white")
l_5.grid(row=1, column=0, padx=(0,350), pady=(50,0))
l_6 = Label(root, text=w_6,bg = "black", fg="white")
l_6.grid(row=1, column=0, padx=(0,250), pady=(50,0))

e_1 = Entry(root)
e_1.grid(row=3, column=0)

e_1.bind("<space>", check)
root.bind("<Key>", color_red)













root.mainloop()

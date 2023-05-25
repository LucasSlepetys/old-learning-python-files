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


if space == 1:
    check_color(l_2, w_2)
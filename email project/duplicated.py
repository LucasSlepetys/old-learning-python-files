
listEmail = []

def removeDup(file):
    with open(file) as f:
        for line in f:
            listEmail.append((line.split("\n")[0]).lower())

        newList = list(set(listEmail))
    
    with open('nowDup.txt', 'w') as f:
        for email in newList:
            f.write(email)
            f.write('\n')


removeDup("halloween_email.txt")
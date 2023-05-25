#Defining a function to find the word:
def find_word(word_old, word_new, file_name):
    f = open(file_name, "r")
    f_content = f.read().split()
    f.close()
    word = word_old
    with open(file_name, "w") as file:
        for word in f_content:
            file.write(word.replace(word_old, word_new))
#Taking word_old, word_new and file name from user:
def replace_word():
    file_name = input("Please enter the name of your textfile: ")
    word_old = input("Enter any word you want to replace: ")
    word_new = input("Enter the word that " + "'" + word_old + "'" + " will be replaced to: ")
    find_word(word_old, word_new, file_name)
    return (word_old + " was replaced with: " + word_new)
#Calling final function to run the codes:
replace_word()
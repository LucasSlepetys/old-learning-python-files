#Defining a function to replace letters:
def replace(old, new, textfile_name):
    f = open(textfile_name, "r")
    f_content = f.read()
    f.close()
    print(f_content)
    with open(textfile_name, "w") as file:
        for i in f_content:
            file.write(i.replace(old, new))
#Defining the letters that will be replaced:
def replacing():
    textfile = str(input("Please enter the name of your textfile: "))
    old_character = str(input("Which character do you want to replace: "))
    new_character = str(input("Which character do you want " + "'" + old_character + "'" + " to be replaced to? "))
    replace(old_character, new_character, textfile)
    return (old_character + " was replaced with: " + new_character)  
#Calling the funtions to replace the selected letters: 
replacing()
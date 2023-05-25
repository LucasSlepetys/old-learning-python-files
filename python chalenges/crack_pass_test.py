from random import * 

user_pass = input("Enter your password: ")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

guess = ""
len_password = len(password)
x = 0
previous_pass = []
same_attempt = 0
passw = ''
same_guess = []

while (guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, len_password - 1)]
        guess = str(guess_letter)  + str(guess)
        

    for i in previous_pass:
        passw = i
        if guess == passw:
            # print(guess + "----" + i)
            same_attempt += 1
            same_guess.append(guess)
            break    

    previous_pass.append(guess)
    print(guess)
            

    x += 1

print("Your password is: " + guess)
print("It took " + str(x) + " times to find your password!")
print("You tried the same password " + str(same_attempt) + " times")
# print("\n" + "\n")
# print(previous_pass)
# print("\n" + "\n")
# print(same_guess)
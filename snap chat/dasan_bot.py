import pyautogui as pyauto
import time

global xposes
global yposes
xposes = []
yposes = []

def findpos(times):
    for i in range(times):
        times = times - 1
        print("Go to mouse position!")
        time.sleep(1)
        print("Taking mouse cordinates in:")
        time.sleep(1)
        y = 5
        for i in range(5):
            print(y)
            time.sleep(1)
            y -= 1
        pos = pyauto.position()
        pos = str(pos)
        pos = pos.split("=") 
        print(pos)
        #! -----------------------------------
        first = 0
        for i in pos:
            first += 1
            if first == 2:
                x = i.split(",")
                for i in x:
                    print(i)
                    xposes.append(i)
                    break
            elif first == 3:
                x = i.split(")")
                for i in x:
                    print(i)
                    yposes.append(i)
                    break
        #! -----------------------------------
        if times > 0: 
            print("Next mouse position:")
        else:
            time.sleep(2)
            print("Position has been saved!")
            

times = int(input("Enter number of mouse position you would like to take... It should be 6.... -->")) 
findpos(times)

times = int(input("This loop will repeat 10 * x times... So if you say that x is = 1... It will repeat 10 times... If x is = to 2... It will repeat 20 times..." + "\n" + "Enter the value of x:"))
start = ""
while True:
    if start == "start":
        for ii in range(times):
            for i in range(10):
                time.sleep(1)
                pyauto.moveTo(int(xposes[0]),int(yposes[0]))

                for i in range(8):
                    pyauto.click()
                    time.sleep(1)

                pyauto.moveTo(int(xposes[1]),int(yposes[1]))
                pyauto.click()

                time.sleep(1)

                pyauto.moveTo(int(xposes[2]),int(yposes[2]))
                pyauto.click()

                time.sleep(2)

                pyauto.moveTo(int(xposes[3]),int(yposes[3]))
                time.sleep(1)
                pyauto.click()

                pyauto.moveTo(int(xposes[4]),int(yposes[4]))
                pyauto.click()

                time.sleep(5)
                pyauto.moveTo(int(xposes[5]),int(yposes[5]))
                pyauto.click()
                time.sleep(1)
            time.sleep(15)
    else:
        print("To start the program, enter the word 'start'... To stop the program, close the terminal or whatever you are using to run this...")
        start = input("Enter 'start' to start the loop --->")
    
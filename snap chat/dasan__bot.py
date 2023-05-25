import pyautogui as pyauto
import time

def findpos(times):
    for i in range(times):
        times = times - 1
        print("Go to mouse position!")
        time.sleep(1)
        print("Taking mouse cordinates in:")
        time.sleep(1)
        y = 10
        for i in range(2):
            print(y)
            time.sleep(1)
            y -= 1
        pos = pyauto.position()
        print(pos)

        pos = str(pos)
        pos = pos.split("=") 
        print(pos)

        global xposes
        global yposes
        xposes = []
        yposes = []
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
            time.sleep(1)
            print("Save this position somewhere!!!! You have 10s")
            time.sleep(11)        
            print("Next mouse position:")
        else:
            time.sleep(2)
            print("Save this position somewhere!!!!")
            

times = int(input("Enter number of mouse position you would like to take... It should be 6.... -->")) 
findpos(times)

pyauto.moveTo(int(xposes[0]),int(yposes[0]))
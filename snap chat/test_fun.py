import pyautogui as pyauto
import time

# def findpos(times):
#     for i in range(times):
#         times = times - 1
#         print("Go to mouse position!")
#         time.sleep(2)
#         print("Go to mouse position!")
#         time.sleep(1)
#         print("Taking mouse cordinates in:")
#         time.sleep(1)
#         y = 10
#         for i in range(10):
#             print(y)
#             time.sleep(1)
#             y -= 1
#         pos = pyauto.position()
#         print(pos)
#         if times > 0:
#             time.sleep(1)
#             print("Save this position somewhere!!!!")
#             time.sleep(10)        
#             print("Next mouse position:")
#         else:
#             time.sleep(2)
#             print("Save this position somewhere!!!!")
#             

# times = int(input("Enter number of mouse position you would like to take:")) 
# findpos(times)

# print("\n" + "\n")

# print("<<<<<--- Now that you have the mouse positions, let's enter them and especify how many times you would like to click on them... And then their interval between each position --->>>>>")

global posx_list
global posy_list

posx_list = []
posy_list = []
def positions(times):
    x = 1
    for i in range(times):
        posx = input("Enter x cordinates of position #" + str(x) + "-->")
        posy = input("Enter y cordinates of position #" + str(x) + "-->")

        posx_list.append(posx)
        posy_list.append(posy)

        x += 1
        print(posx_list)

time.sleep(4)

times = int(input("Enter number of positions you would like to go to in this loop --->" + "\n" + "\n" + "Example: " + "\n" + "if you want to go and click in 6 different positions then type '6'... if you want to go and click in '8' different positions then type 8!" + "\n" + "\n" + "----->")) 
positions(times)


        
    

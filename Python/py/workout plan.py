#Creating dictionaary:
import json
workout = { 
    "Workout": [
        {
        "Exercise": "Push up",
        "Extra Weight in (Kg)": 0,
        "Sets": 1,
        "Reps": 1,
        "Sets * Reps": 0 }
    ]
        }
#Taking user's input:
with open("workout_plan.json", "a") as f:   
    for obj in workout["Workout"]:
        obj["Exercise"] = str(input("Exercise: "))
        obj["Extra Weight in (Kg)"] = int(input("Extra weight (in Kg): "))
        obj["Reps"] = int(input("Reps: "))
        obj["Sets"] = int(input("Sets: "))
        obj["Sets * Reps"] = (obj["Sets"] * obj["Reps"])
        json.dump(workout["Workout"], f, indent = 2)
#Defining a function to replace letters:
def replace(letter):
    f = open("workout_plan.json", "r")
    f_content = f.read()
    f.close()
    print(f_content)
    with open("workout_plan.json", "w") as file:
        for i in f_content:
            file.write(i.replace(letter, " "))
#Defining the letters that will be replaced:
def replacing():
    replace("{")
    replace("}")
    replace("[")
    replace("]")
    replace('"')
    replace(',')
    return ("'{', '}', '[', ']' were replaced with air")     
#Calling the funtions to replace the selected letters:
replacing()
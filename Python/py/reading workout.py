import json
content = "EX"
with open("workout_plan.json", "r+") as f:
    f_content = f.read()
    for i in f_content:
        if i == 20:
            f.write(content)
            
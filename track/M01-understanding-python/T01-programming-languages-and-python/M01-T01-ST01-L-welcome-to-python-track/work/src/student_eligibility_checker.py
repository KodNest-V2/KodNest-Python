marks = int(input())
attendance = int(input())
project_completed = input()

if marks >= 60 and attendance >= 75:
    if project_completed == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
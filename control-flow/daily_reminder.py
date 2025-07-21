task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        print("Invalid priority level entered.")
        exit()

if time_bound == "yes":
    if priority == "low":
        # low priority but time bound — just say immediate attention anyway
        reminder += " that requires immediate attention today!"
    else:
        reminder += " that requires immediate attention today!"
elif time_bound == "no":
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += "."
else:
    print("Invalid input for time-bound (yes/no).")
    exit()

print(reminder)

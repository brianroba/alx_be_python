task = input("Enter a task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: Your HIGH priority task '{task}'"
    case "medium":
        reminder = f"Reminder: Your MEDIUM priority task '{task}'"
    case "low":
        reminder = f"Reminder: Your LOW priority task '{task}'"
    case _:
        print("Invalid priority level entered.")
        exit()

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += " — no immediate rush."


# Optional: Repeat the reminder 3 times to demonstrate loop usage
for _ in range(3):
    print(reminder)

def get_priority():
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            return priority
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

def get_time_bound():
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ("yes", "no"):
            return time_bound
        print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    task = input("Enter your task: ").strip()
    priority = get_priority()
    time_bound = get_time_bound()

    # Use match case for priority (just for demonstration)
    match priority:
        case "high":
            pass
        case "medium":
            pass
        case "low":
            pass

    # Print based on time_bound
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()

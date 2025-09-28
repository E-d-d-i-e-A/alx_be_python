# Personal Daily Reminder
# This program provides customized task reminders based on priority and time sensitivity

def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Process the task based on priority using Match Case
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' is a task"
    
    # Modify reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
        print(f"Reminder: {reminder}")
    else:
        if priority == "high":
            reminder += ". Focus on completing it today!"
        elif priority == "medium":
            reminder += ". Try to complete it today."
        else:
            reminder += ". Consider completing it when you have free time."
        print(f"Note: {reminder}")

if __name__ == "__main__":
    main()

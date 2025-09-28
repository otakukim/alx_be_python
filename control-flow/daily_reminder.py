task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a HIGH priority task that requires immediate attention!")
        else:
            print(f"Reminder: '{task}' is a HIGH priority task but not time-bound.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a MEDIUM priority task with a deadline. Complete it soon.")
        else:
            print(f"Note: '{task}' is a MEDIUM priority task. You can schedule it flexibly.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a LOW priority task but time-bound. Finish it on time.")
        else:
            print(f"Note: '{task}' is a LOW priority task and not urgent.")
    case _:
        print("Invalid priority entered.")

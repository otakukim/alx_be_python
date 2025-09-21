task = input("Enter your task :")
priority = input("Enter task priority(high, medium ,low,) :")
time_bound = input("is it time bound ?(yes/no) :")
match priority:
    case "high": 
        if time_bound == "yes" :
            print(f" Reminder :{task} is a high priority task that requires immediate attention today")        
        else :
            print(f" Reminder :{task} is a high priority task that is not time bound")   
    case "medium":
        if time_bound == "yes":
            print(f" Reminder: {task} is a medium priority task with a deadline. Don’t delay too much.")
        else:
            print(f" Note: {task} is medium priority and flexible. Fit it into your schedule.")
    case "low" :
         if time_bound == "yes":
            print(f" Note : {task} is a low priority task. Consider completing it when you have free time ")
         else :
            print(f" Note : {task} is a low priority task that is not time bound")
    case _: 
        print("Invalid priority entered.")


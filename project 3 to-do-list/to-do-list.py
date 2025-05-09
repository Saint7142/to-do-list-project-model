#data
tasks = [] 
stage = []
#input
while True:
    method = input("To-do-list(press 1), Exit(press 2): ")
    if method == "1":
        task = input(f"Enter task. {len(tasks)+1}: ")
        tasks.append(task)
    elif method == "2":
        print("End of program")
        break
    else:
        print("This key isn't available")
#display 
if tasks:
    print("\nYour task: ")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
else:
    print("No added to-do-list")
#checking task
while True:
    check = input("checking(press 1), not yet(press 2), checking done(press 3): ")
    if check == "1":
        try:
            task_num = int(input("Enter the task number to mark as finished: "))
            if 1 <= task_num <= len(tasks):  
                stage.append("Finished")
                print(f"{task_num}. {tasks[task_num - 1]}: finished")
            else:
                print("Invalid task number.")  
        except ValueError:
            print("Please enter a valid number.")  
    elif check == "2":
        try:
            task_num = int(input("Enter the task number to mark as not finished: "))
            if 1 <= task_num <= len(tasks): 
                stage.append("Unfinished")
                print(f"{task_num}. {tasks[task_num - 1]}: not finished yet")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    elif check == "3":
        for i, task in enumerate(tasks):  
            print(f"{i+1}. {task} status: {stage[i]}")
        break
    else:
        print("This key isn't available", "End of service")
        break
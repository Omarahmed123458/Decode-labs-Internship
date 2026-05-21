print("Welcome to the to-do list program")
choice = 0
Tasks_list = []
while choice!="4":
    print("Type 1 if you want to add a task")
    print("Type 2 if you want to review a task")
    print("Type 3 if you want to delete a task")
    print("Type 4 if you want to exit")
    choice = input()
    if choice == "1":
        x = input("Enter the task name: ")
        y = input("The task ID: ")
        duplication = False 
        for task in Tasks_list:
            if task["id"] == y:
                print("This ID already exists for a task, try another ID")
                duplication = True 
                break
        if(duplication==False): 
            z = {"id":y,"name":x}
            Tasks_list.append(z)
    elif choice == "2":
        print("Your tasks are: ")
        if(len(Tasks_list)==0):
            print("No tasks added yet")
        else:   
            for index,task in enumerate(Tasks_list, start = 1):
                print(f"{index}. ID: {task["id"]} | Task: {task["name"]}")
    elif choice == "3":
        if(len(Tasks_list)==0):
            print("No tasks added yet")
        task_to_delete = input("Enter the ID of the task that you want to delete ")
        for task in Tasks_list:
            if task["id"]==task_to_delete:
                 Tasks_list.remove(task)
                 break
    elif choice == "4":
        print("Good bye") 
    else:
        print("Incorrect number, Please enter a number from above")

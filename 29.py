def holiday_checklist():
    
    destination = input("Enter the destination of your holiday: ")

    num_items = int(input("How many things do you need to pack? "))
    num_tasks = int(input("How many tasks do you need to complete before your holiday? "))

 
    packing_list = []
    for i in range(num_items):
        item = input(f"Enter item {i + 1} to pack: ")
        packing_list.append(item)


    task_list = []
    for i in range(num_tasks):
        task = input(f"Enter task {i + 1} to complete: ")
        task_list.append(task)

    print(f"\nHoliday Checklist for {destination}:")

    print("\nThings to pack:")
    for item in packing_list:
        print(f"- {item}")

    print("\nTasks to complete:")
    for task in task_list:
        print(f"- {task}")


holiday_checklist()

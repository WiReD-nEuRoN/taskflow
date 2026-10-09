tasks = []
completed_tasks = []

print("Welcome to the TaskFlow!")

while True:
    print("\n***TaskFlow***")
    print("1. Add task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        task = input("Enter Task: ")
        tasks.append(task)
        completed_tasks.append(False)
        print("Task added!")

    elif choice == 2:
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No Tasks yet!")
        for i in range(len(tasks)):
            if completed_tasks[i] == True:
                print(i+1,".", tasks[i], "- Done")
            else:
                print(i+1,".", tasks[i], "- Pending")

    elif choice == 3:
        num = int(input("Enter Task Number: "))

        if num >=1 and num <= len(tasks):
            completed_tasks[num - 1] = True
            print("Task Done.")
        else:
            print("Invalid Task Number")

    elif choice == 4:
        print("Thanks for using TaskFlow")
        break

    else:
        print("Invalid Choice")

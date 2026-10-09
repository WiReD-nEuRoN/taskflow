tasks = []
completed_tasks = []
priorities = []
deadlines = []

try:
    file = open("tasks.txt", "r")

    for line in file:
        data = line.strip().split("|")

        tasks.append(data[0])
        completed_tasks.append(data[1]=="True")
        priorities.append(data[2])
        deadlines.append(data[3])

    file.close()
except FileNotFoundError:
    pass


print("Welcome to the TaskFlow!")

while True:
    print("\n***TaskFlow***")
    print("1. Add task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Task Statistics")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        task = input("Enter Task: ")

        if task.strip() == "":
            print("Task can't be empty.")

        print("Choose Priority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        p_choice = int(input("Enter Priority: "))

        if p_choice == 1:
            priority = "High"
        elif p_choice == 2:
            priority = "Medium"
        elif p_choice == 3:
            priority = "Low"
        else:
            priority = "Medium"

        deadline = input("Enter Deadline (DD-MM-YYYY): ")
        tasks.append(task)
        completed_tasks.append(False)
        priorities.append(priority)
        deadlines.append(deadline)

        print("Task added!")

    elif choice == 2:
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No Tasks yet!")
        for i in range(len(tasks)):
            if completed_tasks[i] == True:
                status = "Done"
            else:
                status = "Pending"

            print("\nTask: ",i+1)
            print("Name: ", tasks[i])
            print("Status: ", status)
            print("Priority: ", priorities[i])
            print("Deadline: ", deadlines[i])

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            num = int(input("Enter Task number: "))

            if num >= 1 and num <= len(tasks):
                completed_tasks[num-1] = True
                print("Task Completed.")
            else:
                print("Invalid task number.")

    elif choice == 4:
        if len(tasks) == 0:
            print("No task to delete.")
        else:
            num = int(input("Enter Task Number: "))

        if num >= 1 and num <= len(tasks):
            tasks.pop(num-1)
            completed_tasks.pop(num-1)
            priorities.pop(num-1)
            deadlines.pop(num-1)

            print("Task deleted!")

        else:
            print("Invalid task number.")

    elif choice == 5:
        total = len(tasks)
        done = 0
        pending = 0

        for i in range(len(tasks)):
            if completed_tasks[i] == True:
                done += 1
            else:
                pending += 1

        print("\n***Task Stastics***")
        print("Total Tasks: ",total)
        print("Completed Tasks: ",done)
        print("Pending Tasks: ", pending)

        if total > 0:
            percentage = (done/total)*100
            print("Complettion: ",round(percentage, 2),"%")
        else:
            print("Completion 0%")

    elif choice == 6:
        file = open("tasks.txt", "w")

        for i in range(len(tasks)):
            file.write(
                tasks[i] + "|" +
                str(completed_tasks[i]) + "|" +
                priorities[i] + "|" +
                deadlines[i] + "\n"
            )
        file.close()
        print("Tasks Saved")
        print("Thanks for using TaskFlow")
        break

    else:
        print("Invalid Choice")

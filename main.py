import datetime

tasks = []
completed_tasks = []
priorities = []
deadlines = []
notes = []
categories = []

try:
    file = open("tasks.txt", "r")

    for line in file:
        data = line.strip().split("|")

        tasks.append(data[0])
        completed_tasks.append(data[1]=="True")
        priorities.append(data[2])
        deadlines.append(data[3])

        if len(tasks) >= 5:
            notes.append(tasks[4])
        else:
            notes.append("")

        if len(data)>=6:
            categories.append(data[5])
        else:
            categories.append("General")

    file.close()
except FileNotFoundError:
    pass


print("Welcome to the TaskFlow!")

while True:
    print("\n"+"="*35)
    print("         TaskFlow")
    print("         Your Task Manager")
    print("="*35)

    total = len(tasks)
    done = 0

    for i in range(len(tasks)):
        if completed_tasks[i] == True:
            done += 1
    pending = total - done

    if pending > 0:
        print("Reminder:", pending, "task(s) still pending.")
    else:
        print("Great! All tasks completed.")

    print("Total Tasks:", total)
    print("Completed:", done)
    print("Pending:", pending)

    if total > 0:
        percentage = (done/total)*100
        filled_blocks = int((done/total)*10)
        empty_blocks = 10 - filled_blocks

        progress_bar = "["

        for i in range(filled_blocks):
            progress_bar = progress_bar + "#"

        for i in range(empty_blocks):
            progress_bar = progress_bar + "-"

        progress_bar = progress_bar + "]"

        print("\n---Task Progress---")
        print("Progress:", progress_bar, round(percentage,1),"%")
        print("Completed:", done, "/",total,"tasks") 
    else:
        print("\n---Task Progress---")
        print("Progress: [------------] 0%")
        print("Completed: 0/0 tasks")

    print("="*35)

    print("1. Add task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Task Statistics")
    print("6. Search Tasks")
    print("7. Filter Tasks")
    print("8. Sort Tasks")
    print("9. Deadline Alerts")
    print("10. Edit Tasks")
    print("11. Exit")
    print("-"*35)

    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Invalid input. Please Enter a number")
        continue

    if choice == 1:
        task = input("Enter Task: ")
        note = input("Enter task notes(Optional): ")
        notes.append(note)

        if task.strip() == "":
            print("Task can't be empty.")

        print("Choose Priority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        try:
            p_choice = int(input("Enter Priority: "))
        except ValueError:
            p_choice = 2
            print("Invalid input. Medium priority Selected")

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

        print("\nChoose Category:")
        print("1. School")
        print("2. Robotics")
        print("3. Coding Projects")
        print("4. Personal")
        print("5. General")

        category_chc = int(input("Enter Category: "))

        if category_chc == 1:
            category = "School"
        elif category_chc == 2:
            category = "Robotics"
        elif category_chc == 3:
            category = "Coding Projects"
        elif category_chc == 4:
            category = "Personal"
        else:
            category = "General"

        categories.append(category)

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
            print("Category: ", categories[i])

            if notes[i] != "":
                print("Notes: ", notes[i])
            else:
                print("Notes: None")

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            try:
                num = int(input("Enter Task Number: "))
            except ValueError:
                num = 0
                print("Please enter a valid task number.")

            if num >= 1 and num <= len(tasks):
                completed_tasks[num-1] = True
                print("Task Completed.")
            else:
                print("Invalid task number.")

    elif choice == 4:
        if len(tasks) == 0:
            print("No task to delete.")
        else:
            try:
                num = int(input("Enter Task Number: "))
            except ValueError:
                num = 0
                print("Please enter a valid task number.")

        if num >= 1 and num <= len(tasks):
            tasks.pop(num-1)
            completed_tasks.pop(num-1)
            priorities.pop(num-1)
            deadlines.pop(num-1)
            notes.pop(num-1)
            categories.pop(num-1)

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
        srch = input("Enter task name to search: ").lower()
        found = False

        for i in range(len(tasks)):
            task_name = tasks[i].lower()
            task_notes = notes[i].lower()
            task_category = categories[i].lower()

            if (srch in task_name or
                srch in task_notes or
                srch in task_category):

                print("\nTask:",i+1)
                print("Name:",tasks[i])
                print("Category:",categories[i])
                print("Priority:",priorities[i])
                print("Deadline:",deadlines[i])
                print("Notes:",notes[i])

                if completed_tasks[i] == True:
                    print("Status: Done")
                else:
                    print("Status: Pending")

                found = True

        if found == False:
            print("No matching tasks found")

    elif choice == 7:
        print("1. High Priority")
        print("2. Medium Priority")
        print("3. Low Priority")
        print("4. Pending Tasks")
        print("5. Completed Tasks")
        print("6. School")
        print("7. Robotics")
        print("8. Coding")
        print("9. Personal")
        print("10. General")

        try:
            filter_chc = int(input("Choose a filter: "))
        except ValueError:
            filter_chc = 0
            print("Invalidd filter. Please choose a number.")
        found = False

        for i in range(len(tasks)):
            if filter_chc == 1 and priorities[i] == "High":
                print(tasks[i], "-",deadlines[i])
                found = True
            elif filter_chc == 2 and priorities[i] == "Medium":
                print(tasks[i], "-", deadlines[i])
                found = True
            elif filter_chc == 3 and priorities[i] == "Low":
                print(tasks[i], "-", deadlines[i])
            elif filter_chc == 4 and completed_tasks[i] == False:
                print(tasks[i],"-",priorities[i])
                found = True
            elif filter_chc == 5 and completed_tasks[i] == True:
                print(tasks[i], "-", priorities[i])
            elif filter_chc == 6 and categories[i] == "School":
                print(tasks[i],"-",deadlines[i])
                found = True
            elif filter_chc == 7 and categories[i] == "Robotics":
                print(tasks[i], "-",deadlines[i])
                found = True
            elif filter_chc == 8 and categories[i] == "Coding":
                print(tasks[i],"-",deadlines[i])
                found = True
            elif filter_chc == 9 and categories[i] == "Personal":
                print(tasks[i],"-",deadlines[i])
                found = True
            elif filter_chc == 10 and categories[i] == "General":
                print(tasks[i],"-",deadlines[i])
                found = True

        if found == False:
            print("No matching tasks")

    elif choice == 8:
        print("\n---Sort Tasks---")
        print("1. Sort by priority")
        print("2. Sort by Deadline")
        print("3. Sort by Status")
        print("4. Sort by Priority and Deadline")

        try:
            sort_chc = int(input("\nChoose sorting method: "))
        except ValueError:
            sort_chc = 0
            print("Invalid sorting choice.")

        if sort_chc == 1 or sort_chc == 2 or sort_chc == 3 or sort_chc == 4:
            for i in range(len(tasks)):
                for j in range(i+1, len(tasks)):
                    swap = False

                    if sort_chc == 1:
                        priority_i = 0
                        priority_j = 0

                        if priorities[i] == "High":
                            priority_i = 1
                        elif priorities[i] == "Medium":
                            priority_i = 2
                        elif priorities[i] == "Low":
                            priority_i = 3

                        if priorities[j] == "High":
                            priority_j = 1
                        elif priorities[j] == "Medium":
                            priority_j = 2
                        elif priorities[j] == "Low":
                            priority_j = 3

                        if priority_i > priority_j:
                            swap = True

                    elif sort_chc == 2:
                        try:
                            deadline_i = datetime.datetime.strptime(
                                deadlines[i].strip(), "%d-%m-%Y"
                            ).date()
                        except ValueError:
                            deadline_j = datetime.date.max

                        if deadline_i > deadline_j:
                            swap = True

                    elif sort_chc == 3:
                        temp = tasks[i]
                        tasks[i] = tasks[j]
                        tasks[j] = temp

                        temp = completed_tasks[i]
                        completed_tasks[i] = completed_tasks[j]
                        completed_tasks[j] = temp

                        temp = priorities[j]
                        priorities[i] = priorities[j]
                        priorities[j] = temp

                        temp = deadlines[i]
                        deadlines[i] = deadlines[j]
                        deadlines[j] = temp

                        temp = notes[i]
                        notes[i] = notes[j]
                        notes[j] = temp

                    elif sort_chc == 4:
                        priority_i = 0
                        priority_j = 0

                        if priorities[i] == "High":
                            priority_i = 1
                        elif priorities[i] == "Medium":
                            priority_i = 2
                        elif priorities[i] == "Low":
                            priority_i = 3

                        if priorities[j] == "High":
                            priority_j = 1
                        elif priorities[j] == "Medium":
                            priority_j = 2
                        elif priorities[j] == "Low":
                            priority_j = 3

                        if priority_i > priority_j:
                            swap = True

                        elif priority_i == priority_j:
                            try:
                                deadline_i = datetime.datetime.strptime(
                                    deadlines[i].strip(), "%d-%m-%Y"
                                ).date()
                            except ValueError:
                                deadline_i = datetime.date.max

                            try:
                                deadline_j = datetime.datetime.strptime(
                                    deadlines[j].strip(), "%d-%m-%Y"
                                ).date()
                            except ValueError:
                                deadline_j = datetime.date.max

                            if deadline_i > deadline_j:
                                swap = True
                        

            print("\nTasks sorted successfully")
            print("\n---Sorted Tasks---")

            if len(tasks) == 0:
                print("No tasks to display.")

            for i in range(len(tasks)):
                if completed_tasks[i] == True:
                    status = "Done"
                else:
                    status = "Pending"

                print("\nTask: ",i+1)
                print("Name: ",tasks[i])
                print("Status: ", status)
                print("Priority: ", priorities[i])
                print("Deadline: ",deadlines[i])
                print("Notes: ",notes[i])

        else:
            print("Invalid Sorting Choice.")            

    elif choice == 9:
        today = datetime.date.today()
        found = False

        print("\n---Deadline Alerts---")

        for i in range(len(tasks)):
            if completed_tasks[i] == False:
                try:
                    today = datetime.date.today()

                    deadline = datetime.datetime.strptime(
                        deadlines[i].strip(), "%d-%m-%Y"
                    ).date()

                    days_left = (deadline - today).days

                    if days_left < 0:
                        print(tasks[i], "- Overdue!")
                        found = True
                    elif days_left == 0:
                        print(tasks[i], "- Due Today!")
                        found = True
                    elif days_left <= 3:
                        print(tasks[i], "- Due in", days_left, "day(s)")
                        found = True
                except ValueError:
                    print("Invalid deadline for:", tasks[i])
                    print("Stored deadline:", repr(deadlines[i]))

        if found == False:
                print("No urgent deadlines. Yeay!")

    elif choice == 10:
        if len(tasks) == 0:
            print("No tasks available to edit.")
        else:
            print("\n---Edit Task---")

            for i in range(len(tasks)):
                print(i+1,".",tasks[i])

            num = int(input("Enter task number to edit: "))

            if num >= 1 and num <= len(tasks):
                print("\nSelected Task: ", tasks[num-1])
                print("1. Edit Task Name")
                print("2. Edit Notes")
                print("3. Edit priority")
                print("4. Edit Deadline")
                print("5. Edit Category")

                edit_chc = int(input("Choose what to edit: "))

                if edit_chc == 1:
                    new_name = input("Enter new task name: ")

                    if new_name.strip() == "":
                        print("Task name cannot be empty.")
                    else:
                        tasks[num-1] = new_name
                        print("Task name updated")
                elif edit_chc == 2:
                    new_note = input("Enter new note: ")
                    notes[num-1] = new_note
                    print("Note Updated!")

                elif edit_chc == 3:
                    print("\nChoose new priority")
                    print("1. High")
                    print("2. Medium")
                    print("3. Low")

                    p_chc = int(input("Enter priority: "))

                    if p_chc == 1:
                        priorities[num-1] = "High"
                        print("Priority Updated.")
                    elif p_chc == 2:
                        priorities[num-1] = "Medium"
                        print("Priorities Updated.")
                    elif p_chc == 3:
                        priorities[num-1] = "Low"
                        print("Priorities Updated.")
                    else:
                        print("Invalid Choice")

                elif edit_chc == 4:
                    new_deadline = input("Enter new deadline(DD-MM-YYYY): ")

                    try:
                        datetime.datetime.strptime(
                            new_deadline.strip(), "%d-%m-%Y"
                        )

                        deadlines[num-1] = new_deadline.strip()
                        print("Deadline Updated")
                    except ValueError:
                        print("Inavlid Date Format!")
                        print("Please use DD-MM-YYYY")

                elif edit_chc == 5:
                    print("\nChoose New Category: ")
                    print("1. School")
                    print("2. Robotics")
                    print("3. Coding")
                    print("4. Personal")
                    print("5. General")

                    category_chc = int(input("Enter Category: "))

                    if category_chc == 1:
                        categories[num-1] = "School"
                        print("Category Updated.")
                    elif category_chc == 2:
                        categories[num-1] = "Robotics"
                        print("Category Updated.")
                    elif category_chc == 3:
                        categories[num-1] = "Coding"
                        print("Category Updated")
                    elif category_chc == 4:
                        categories[num-1] = "Perrsonal"
                    elif category_chc == 5:
                        categories[num-1] = "General"
                    else:
                        print("Invalid Choice.")


                else:
                    print("Invalid Edit Choice.")
            else:
                print("Invalid task number")

    elif choice == 11:
        file = open("tasks.txt", "w")

        for i in range(len(tasks)):
            file.write(
                tasks[i] + "|" +
                str(completed_tasks[i]) + "|" +
                priorities[i] + "|" +
                deadlines[i] + "|" +
                notes[i] + "|" +
                categories[i] + "\n"
            )
        file.close()
        print("Tasks Saved")
        print("Thanks for using TaskFlow")
        break

    else:
        print("Invalid Choice")


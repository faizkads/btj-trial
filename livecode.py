# To-Do List App
# Faiz Khansa Adrika
import json

#CONFIGURE FILENAME FIRST
#************************
nfile = "todo.txt"     #*
#************************

def view_task():

    print("Your tasks: ")
    with open(nfile, "r") as file:
        tasks =  file.readlines()
        for task in tasks:
            temp_task =  json.loads(task)
            print(f"Nama: {temp_task["name"]} | Priority: {temp_task["priority"]} | Status: {temp_task["status"]}")

def filter_view(): #Untuk menampilkan task dengan filter dari status
    status_task = input("Pilih status task (To Do, In Progress, Done): ")

    with open(nfile, "r") as file:
        tasks = file.readlines()

        for task in tasks:
            temp_task = json.loads(task)
            if temp_task["status"] == status_task: #Jika status task sesuai dengan status yang di input, maka tampilkan
                print(f"Nama: {temp_task["name"]} | Priority: {temp_task["priority"]} | Status: {temp_task["status"]}")

def add_task():
    task = input("Enter your task name: ")
    priority = input("Enter the task priority (High, Medium, Low): ")
    new_task = {
        "name" : task,
        "priority" : priority,
        "status" : "To Do"
    }

    print(new_task, "\nIni adalah new task")

    with open(nfile, "a") as file:
        temp = json.dumps(new_task)
        file.write(temp+"\n")

    print("Note added succesfully")

def delete_task():
    view_task()
    task_del = input("Enter task name to delete: ")
    
    with open(nfile, "r") as file:
        tasks = file.readlines()

        for task in tasks:
            temp_task =  json.loads(task)

            if temp_task["name"] == task_del: #kalau nama task sesuai dengan nama input, maka hapus
                tasks.remove(task)
                break
    
        with open(nfile, "w") as new_file:
            new_file.writelines(tasks) #menulis perubahan (task yang sudah diremove)

def change_status():
    view_task()
    
    chg_task = input("Enter task name to change status: ")

    with open(nfile,"r") as file:
        tasks = file.readlines()
        new_task = []

        for task in tasks:
            temp_task = json.loads(task)

            if temp_task["name"] == chg_task: #jika nama task sesuai dengan input
                
                # Mengubah status task sesuai urutan
                # To Do -> In progress -> Done
                if temp_task["status"] == "To Do":
                    temp_task["status"] = "In Progress"
                elif temp_task["status"] == "In Progress":
                    temp_task["status"] = "Done"
                else:
                    print("Cannot change status, task is done")
                    return
            new_task.append(json.dumps(temp_task)+"\n")
        
        with open(nfile, "w") as new_file:
            new_file.writelines(new_task)
    
    print("Status changed successfully")
    view_task()

def done_percentage():
    
    done_percentage = 0

    with open(nfile, "r") as file:
        tasks = file.readlines()
        done_task = []
        all_task = []
        for task in tasks:
            temp_task = json.loads(task)
            if temp_task["status"] == "Done":
                done_task.append(json.dumps(temp_task)+"\n")
            all_task.append(json.dumps(temp_task)+"\n")
        done_percentage = len(done_task) / len(all_task) * 100
        print(f"{len(done_task)} / {len(all_task)}")
    print(f"Done percentage = {done_percentage}%")



while True:
    print("\nMenu")
    print("1. Add task")
    print("2. View task")
    print("3. Change task status")
    print("4. Delete task")
    print("5. Filtered view")
    print("6. Done percentage")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        change_status()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        filter_view()
    elif choice == "6":
        done_percentage()
    elif choice == "7":
        print("Exit app")
        break
    else:
        print("Invalid choice, enter the number specified in the menu.")

    

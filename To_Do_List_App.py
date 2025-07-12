todo_list=[]

def show_menu():
    print("\n=====TO-DO LIST MENU=====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def add_task():
    task=input("Enter task:")
    todo_list.append({"task":task,"done":False})
    print("✔ Task Added")

def view_tasks():
    if not todo_list:
        print("No tasks yet")
    else:
        for i,task in enumerate(todo_list):
            if isinstance(task,dict):

                status="✔" if task.get("done",False) else"❌"
                print(f"{i+1}.{task.get('task')}[{status}]")
            else:
                print(f"{i+1}.❌ Invalid task Format")

def remove_task():
    view_tasks()
    try:
        index=int(input("Enter task number to remove:"))-1
        removed=todo_list.pop(index)
        print(f"🗑 Remove:{removed['task']}")
    except(ValueError,IndexError):
        print("❌ Invalid number!")

def mark_completed():
    view_tasks()
    try:
        index=int(input("Enter task number to mark as Done:"))-1
        todo_list[index]["done"]=True
        print(f"✔ Marked '{todo_list[index]['task']}'as completed.")
    except(ValueError,IndexError):
        print("❌ Invalid number!")
        
while True:
    show_menu()
    choice=input("Enter your choice: ")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        remove_task()
    elif choice=="4":
        mark_completed()
    elif choice=="5":
        print("👋Exiting... Bye!")
        break
    else:
        print("Invalid choice, please select 1-5.")


def display():
    print("to-do list")
    print("1.view list")
    print("2.add list")
    print("3.update list")
    print("4.remove list")
    print("5.mark as completed")
    print("6.exit")

def view_tasks(tasks):
    if not tasks:
        print("there are no taskes in your list")
    else:
        for i,tasks in enumerate(tasks ,1):
            status="completed" if tasks['completed'] else "not completed"
            print(f"{i},{tasks['description']}-{status}")

def add_tasks(tasks):
    description=input("enter the list")
    tasks.append({"description":description,"completed": False})
    print("task added")

def update_tasks(tasks):
    view_tasks(tasks)
    task_number=int(input("enter the task number for update"))-1
    if 0<=task_number<len(tasks):
        description=input("enter the new description")
        tasks[task_number]['description']=description
        print("task updated")
    else:
        print("invalid number")

def remove_tasks(tasks):
    view_tasks(tasks)
    task_number=int(input("enter the task_number"))-1
    if 0<=task_number<len(tasks):
        tasks.pop(task_number)
        print("task removed")
    else:
        print("invalid task number")

def mark_tasks(tasks):
    view_tasks(tasks)
    task_number=int(input("enter the tasks number"))-1
    if 0<=task_number<len(tasks):
        tasks[task_number]['completed']=True
        print("task marked as completed")
    else:
        print("invalid task number")

def main():
    tasks=[]
    while True:
        display()
        choice=int(input("enter the choice"))
        if choice==1:
            view_tasks(tasks)
        elif choice==2:
            add_tasks(tasks)
        elif choice==3:
            update_tasks(tasks)
        elif choice==4:
            remove_tasks(tasks)
        elif choice==6:
            print("exit a to-do application")
            break
        else:
            print("invlid number")

if __name__=="__main__":
    main()

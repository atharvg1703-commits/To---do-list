import time
import sys

try:
    import colors
    GREEN = colors.green
    BLUE = colors.blue
    YELLOW = colors.yellow
    RED = colors.red
    CYAN = colors.cyan
    OFF = colors.off
except:
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    OFF = "\033[0m"

def slow_print(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()
def fast_print(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()




task1 = ""
task2 = ""
task3 = ""
task4 = ""
task5 = ""

status1 = "todo"
status2 = "todo"
status3 = "todo"
status4 = "todo"
status5 = "todo"

slow_print(CYAN + "===== WELCOME TO TODO LIST ====="+ OFF)
time.sleep(0.2)

while True:
    slow_print(GREEN + "\n===== TODO LIST MENU ====="+ OFF)
    fast_print(BLUE + "1. Add task"+ OFF)
    fast_print(BLUE + "2. Update task"+ OFF)
    fast_print(BLUE + "3. Delete task"+ OFF)
    fast_print(BLUE + "4. Mark task as in progress"+ OFF)
    fast_print(BLUE + "5. Mark task as done"+ OFF)
    fast_print(BLUE + "6. List all tasks"+ OFF)
    fast_print(BLUE + "7. Exit"+ OFF)
    slow_print(GREEN + "=========================="+ OFF)
    
    choice = input(BLUE + "> " + OFF)
    
    if choice == "1":
        num = input(YELLOW + "> Task number (1-5): " + OFF)
        title = input(YELLOW + "> Task title: " + OFF)
        print(YELLOW + "thinking......" + OFF)
        time.sleep(0.5)
        
        if num == "1":
            task1 = title
            print(GREEN + "Task 1 added!" + OFF)
        elif num == "2":
            task2 = title
            print(GREEN + "Task 2 added!" + OFF)
        elif num == "3":
            task3 = title
            print(GREEN + "Task 3 added!" + OFF)
        elif num == "4":
            task4 = title
            print(GREEN + "Task 4 added!" + OFF)
        elif num == "5":
            task5 = title
            print(GREEN + "Task 5 added!" + OFF)
    
    elif choice == "2":
        num = input(YELLOW + "> Task number (1-5): " + OFF)
        title = input(YELLOW + "> New title: " + OFF)
        
        if num == "1":
            task1 = title
            print(GREEN + "Task 1 updated!" + OFF)
        elif num == "2":
            task2 = title
            print(GREEN + "Task 2 updated!" + OFF)
        elif num == "3":
            task3 = title
            print(GREEN + "Task 3 updated!" + OFF)
        elif num == "4":
            task4 = title
            print(GREEN + "Task 4 updated!" + OFF)
        elif num == "5":
            task5 = title
            print(GREEN + "Task 5 updated!" + OFF)
    
    elif choice == "3":
        num = input(YELLOW + "> Task number (1-5): " + OFF)
        
        if num == "1":
            task1 = ""
            status1 = "todo"
            print(RED + "Task 1 deleted!" + OFF)
        elif num == "2":
            task2 = ""
            status2 = "todo"
            print(RED + "Task 2 deleted!" + OFF)
        elif num == "3":
            task3 = ""
            status3 = "todo"
            print(RED + "Task 3 deleted!" + OFF)
        elif num == "4":
            task4 = ""
            status4 = "todo"
            print(RED + "Task 4 deleted!" + OFF)
        elif num == "5":
            task5 = ""
            status5 = "todo"
            print(RED + "Task 5 deleted!" + OFF)
    
    elif choice == "4":
        num = input(YELLOW + "> Task number (1-5): " + OFF)
        
        if num == "1":
            status1 = "in_progress"
            print(YELLOW + "Task 1 marked as in progress!" + OFF)
        elif num == "2":
            status2 = "in_progress"
            print(YELLOW + "Task 2 marked as in progress!" + OFF)
        elif num == "3":
            status3 = "in_progress"
            print(YELLOW + "Task 3 marked as in progress!" + OFF)
        elif num == "4":
            status4 = "in_progress"
            print(YELLOW + "Task 4 marked as in progress!" + OFF)
        elif num == "5":
            status5 = "in_progress"
            print(YELLOW + "Task 5 marked as in progress!" + OFF)
    
    elif choice == "5":
        num = input(YELLOW + "> Task number (1-5): " + OFF)
        
        if num == "1":
            status1 = "done"
            print(GREEN + "Task 1 marked as done!" + OFF)
        elif num == "2":
            status2 = "done"
            print(GREEN + "Task 2 marked as done!" + OFF)
        elif num == "3":
            status3 = "done"
            print(GREEN + "Task 3 marked as done!" + OFF)
        elif num == "4":
            status4 = "done"
            print(GREEN + "Task 4 marked as done!" + OFF)
        elif num == "5":
            status5 = "done"
            print(GREEN + "Task 5 marked as done!" + OFF)
    
    elif choice == "6":
        print(CYAN + "\n===== ALL TASKS ====="+ OFF)
        
        if task1 != "":
            if status1 == "done":
                print(GREEN + "1. [DONE] " + task1 + OFF)
            elif status1 == "in_progress":
                print(YELLOW + "1. [WORKING] " + task1 + OFF)
            else:
                print(BLUE + "1. [TODO] " + task1 + OFF)
        
        if task2 != "":
            if status2 == "done":
                print(GREEN + "2. [DONE] " + task2 + OFF)
            elif status2 == "in_progress":
                print(YELLOW + "2. [WORKING] " + task2 + OFF)
            else:
                print(BLUE + "2. [TODO] " + task2 + OFF)
        
        if task3 != "":
            if status3 == "done":
                print(GREEN + "3. [DONE] " + task3 + OFF)
            elif status3 == "in_progress":
                print(YELLOW + "3. [WORKING] " + task3 + OFF)
            else:
                print(BLUE + "3. [TODO] " + task3 + OFF)
        
        if task4 != "":
            if status4 == "done":
                print(GREEN + "4. [DONE] " + task4 + OFF)
            elif status4 == "in_progress":
                print(YELLOW + "4. [WORKING] " + task4 + OFF)
            else:
                print(BLUE + "4. [TODO] " + task4 + OFF)
        
        if task5 != "":
            if status5 == "done":
                print(GREEN + "5. [DONE] " + task5 + OFF)
            elif status5 == "in_progress":
                print(YELLOW + "5. [WORKING] " + task5 + OFF)
            else:
                print(BLUE + "5. [TODO] " + task5 + OFF)
        
        if task1 == "" and task2 == "" and task3 == "" and task4 == "" and task5 == "":
            print(YELLOW + "  No tasks yet!" + OFF)
    
    elif choice == "7":
        slow_print(CYAN + "===== BYE! ====="+ OFF)
        break
    
    else:
        print(RED + "Invalid choice. Please enter a number between 1 and 7." + OFF)

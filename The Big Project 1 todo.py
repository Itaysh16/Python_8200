import json

class Task():
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        return f"Title: {self.title}, Priority: {self.priority}, Due Date: {self.due_date}, Completed: {self.completed}"

    def __eq__(self, other):
        return self.title == other.title and self.priority == other.priority and self.due_date == other.due_date


class TaskManager():
    def __init__(self):
        self.tasks= []
        self.load_tasks()
    def add_task(self, title, priority, due_date):
        self.tasks.append(Task(title, priority, due_date)) 

    def save_tasks(self):
        dictionaries_list = []
        for task in self.tasks:
            task_dict = {
                "title": task.title,
                "priority": task.priority,
                "due_date": task.due_date,
                "completed": task.completed
            }
            dictionaries_list.append(task_dict)
        
        with open("task.json", "w", encoding="utf-8") as f:
            json.dump(dictionaries_list, f, ensure_ascii=False, indent=4)

    def load_tasks(self):
        self.tasks = []
        try:
            with open("task.json", "r", encoding="utf-8") as f:
                dictionaries_list = json.load(f)
                for task_dict in dictionaries_list:
                    new_task = Task(
                        task_dict["title"], 
                        task_dict["priority"], 
                        task_dict["due_date"]
                    )
                    if "completed" in task_dict:
                        new_task.completed = task_dict["completed"]
                        
                    self.tasks.append(new_task)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def display_tasks(self):
        if not self.tasks:
            print("There are no tasks in the binder right now.")
            return None
        for task in self.tasks:
            print(task)

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.save_tasks()  # שומר מיד את השינוי לקובץ ה-JSON!
            print(f"Task '{self.tasks[task_index].title}' marked as completed! ✓")
        else:
            print("Error: Invalid task index.")




if __name__ == "__main__":
    print("=== Starting Task Manager App ===")
    
    # יוצרים מופע של הקלסר (טוען אוטומטית משימות קיימות מהקובץ)
    manager = TaskManager()
    
    while True:
        print("\n==============================")
        print("       TASK MANAGER MENU      ")
        print("==============================")
        print("1. Display all tasks")
        print("2. Add a new task")
        print("3. Mark task as completed")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            print("\n--- Current Tasks ---")
            manager.display_tasks()
            
        elif choice == "2":
            print("\n--- Add New Task ---")
            title = input("Enter task title: ")
            priority = input("Enter priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            manager.add_task(title, priority, due_date)
            print("Task added successfully!")
            
        elif choice == "3":
            print("\n--- Mark Task as Completed ---")
            manager.display_tasks()
            if manager.tasks:
                try:
                    # מקבלים מהמשתמש את המספר הסידורי (ממירים ל-int)
                    task_index = int(input("Enter the task number to complete: "))
                    manager.mark_completed(task_index)
                except ValueError:
                    print("Error: Please enter a valid number.")
            
        elif choice == "4":
            print("\nExiting Task Manager. Goodbye!")
            break  # שובר את הלולאה ומסיים את התוכנית
            
        else:
            print("\nInvalid choice! Please choose a number between 1 and 4.")




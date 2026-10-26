import customtkinter as ctk
from tkinter import messagebox
import json

# קובע עיצוב כהה ומודרני מראש
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# --- 1. מחלקת Task שלכם ---
class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.title} | Priority: {self.priority} | Due: {self.due_date}"

# --- 2. מחלקת TaskManager שלכם ---
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, priority, due_date):
        new_task = Task(title, priority, due_date)
        self.tasks.append(new_task)
        self.save_tasks()

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.save_tasks()
            return True
        return False

    def save_tasks(self):
        dictionaries_list = [
            {"title": t.title, "priority": t.priority, "due_date": t.due_date, "completed": t.completed} 
            for t in self.tasks
        ]
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(dictionaries_list, f, ensure_ascii=False, indent=4)

    def load_tasks(self):
        self.tasks = []
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                dictionaries_list = json.load(f)
                if not dictionaries_list:
                    return
                for task_dict in dictionaries_list:
                    new_task = Task(task_dict["title"], task_dict["priority"], task_dict["due_date"])
                    new_task.completed = task_dict.get("completed", False)
                    self.tasks.append(new_task)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

# --- 3. ממשק גרפי מודרני (CustomTkinter) ---
class TaskAppModern(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.manager = TaskManager()

        self.title("Task Manager App")
        self.geometry("600x650")

        # כותרת ראשי
        self.title_label = ctk.CTkLabel(self, text="My Task Manager", font=("Segoe UI", 22, "bold"))
        self.title_label.pack(pady=15)

        # מסגרת להוספת משימה חדשה (Inputs)
        self.add_frame = ctk.CTkFrame(self)
        self.add_frame.pack(pady=10, padx=20, fill="x")

        self.title_entry = ctk.CTkEntry(self.add_frame, placeholder_text="Task Title")
        self.title_entry.pack(pady=5, padx=10, fill="x")

        self.priority_entry = ctk.CTkEntry(self.add_frame, placeholder_text="Priority (High/Medium/Low)")
        self.priority_entry.pack(pady=5, padx=10, fill="x")

        self.due_date_entry = ctk.CTkEntry(self.add_frame, placeholder_text="Due Date (YYYY-MM-DD)")
        self.due_date_entry.pack(pady=5, padx=10, fill="x")

        self.add_btn = ctk.CTkButton(self.add_frame, text="Add New Task", fg_color="#2b8a3e", hover_color="#216e31", command=self.add_task)
        self.add_btn.pack(pady=10)

        # תיבת הצגה למשימות (עם מספור 1, 2, 3...)
        self.textbox = ctk.CTkTextbox(self, width=540, height=200, font=("Consolas", 13))
        self.textbox.pack(pady=10)

        # מסגרת לסימון משימה לפי מספר
        self.complete_frame = ctk.CTkFrame(self)
        self.complete_frame.pack(pady=10, padx=20, fill="x")

        self.index_entry = ctk.CTkEntry(self.complete_frame, placeholder_text="Enter task number to complete (e.g. 1)")
        self.index_entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")

        self.complete_btn = ctk.CTkButton(self.complete_frame, text="Mark Completed", fg_color="#1c7ed6", hover_color="#1864ab", command=self.complete_task_by_number)
        self.complete_btn.pack(side="right", padx=10, pady=10)

        # טעינה ראשונית של המשימות למסך
        self.refresh_list()

    def refresh_list(self):
        """ מעדכן את הטקסט בחלון ומוסיף מספור ברור 1, 2, 3... """
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        
        if not self.manager.tasks:
            self.textbox.insert("end", "No tasks available.\n")
        else:
            for idx, task in enumerate(self.manager.tasks, start=1):
                self.textbox.insert("end", f"{idx}. {task}\n")
                
        self.textbox.configure(state="disabled")

    def add_task(self):
        title = self.title_entry.get().strip()
        priority = self.priority_entry.get().strip() or "Medium"
        due_date = self.due_date_entry.get().strip() or "N/A"

        if not title:
            messagebox.showwarning("Input Error", "Please enter a task title!")
            return

        self.manager.add_task(title, priority, due_date)
        self.refresh_list()

        # ניקוי השדות לאחר ההוספה
        self.title_entry.delete(0, "end")
        self.priority_entry.delete(0, "end")
        self.due_date_entry.delete(0, "end")

    def complete_task_by_number(self):
        num_str = self.index_entry.get().strip()
        if not num_str.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid number!")
            return

        task_num = int(num_str)
        task_index = task_num - 1  # המרה מ-1 לבסיס 0 של פייתון

        if self.manager.mark_completed(task_index):
            self.refresh_list()
            self.index_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Invalid task number!")

if __name__ == "__main__":
    app = TaskAppModern()
    app.mainloop()
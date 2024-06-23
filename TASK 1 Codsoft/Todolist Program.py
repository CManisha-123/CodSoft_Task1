import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry('350x400')
root.resizable(False, False)
root.title('TO DO LIST')
image = Image.open("C:\\Users\\Manisha\\Downloads\\calcu.png")
resized_image = image.resize((350, 400))
photo = ImageTk.PhotoImage(resized_image)
label0 = tk.Label(root, image = photo)
label0.place(x=0, y=0, relheight=1, relwidth=1)
label1 = tk.Label(root, text = 'TO DO LIST')
label1.place(x = 135, y = 20)
listbox1 = tk.Listbox(root, height = 13, width = 30)
listbox1.place(x = 80, y = 70)
tasks = []
def view_tasks():
    listbox1.delete(0, tk.END)
    for task, description, completed in tasks:
        status = 'Done' if completed else 'Not Done'
        listbox1.insert(tk.END, f"{task}: {description} [{status}]")
def add_task():
    task = simpledialog.askstring("Add Task", "Enter task:")
    if task:
        description = simpledialog.askstring("Add Description", "Enter description:")
        if description:
            tasks.append((task, description, False))
            view_tasks()
        else:
            messagebox.showwarning("Warning", "Description cannot be empty!")
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")
def complete_task():
    selected_task_index = listbox1.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task, description, completed = tasks[task_index]
        tasks[task_index] = (task, description, True)
        view_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")
def delete_task():
    selected_task_index = listbox1.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        del tasks[task_index]
        view_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")
button1 = tk.Button(root, text = 'Add Task', command = add_task)
button1.place(x = 90, y = 300)
button2 = tk.Button(root, text='Complete Task', command=complete_task)
button2.place(x=170, y=300)
button3 = tk.Button(root, text='Delete Task', command=delete_task)
button3.place(x=130, y=350)
root.mainloop()
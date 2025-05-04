import tkinter as tk
from tkinter import messagebox
import function
import time

def add_todo():
    todo = entry.get().strip()
    if todo:
        todos = function.get_todos()
        todos.append(todo + "\n")
        function.write_todos(todos)
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Input Error", "Please enter a to-do item.")

def update_listbox():
    listbox.delete(0, tk.END)
    todos = function.get_todos()
    for index, item in enumerate(todos):
        listbox.insert(tk.END, f"{index + 1}. {item.strip()}")

def complete_todo():
    try:
        selected = listbox.curselection()[0]
        todos = function.get_todos()
        item = todos.pop(selected).strip()
        function.write_todos(todos)
        update_listbox()
        messagebox.showinfo("Completed", f"Completed: {item}")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a to-do to complete.")

def edit_todo():
    try:
        selected = listbox.curselection()[0]
        new_text = entry.get().strip()
        if not new_text:
            messagebox.showwarning("Input Error", "Please enter new text to edit.")
            return
        todos = function.get_todos()
        todos[selected] = new_text + "\n"
        function.write_todos(todos)
        update_listbox()
        entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a to-do to edit.")

window = tk.Tk()
window.title("To-Do App (Tkinter GUI)")
window.geometry("400x400")


time_label = tk.Label(window, text="It is " + time.strftime("%b %d, %Y %H:%M:%S"))
time_label.pack(pady=5)


entry = tk.Entry(window, width=40)
entry.pack(pady=5)


add_btn = tk.Button(window, text="Add", width=10, command=add_todo)
add_btn.pack(pady=2)

edit_btn = tk.Button(window, text="Edit", width=10, command=edit_todo)
edit_btn.pack(pady=2)

complete_btn = tk.Button(window, text="Complete", width=10, command=complete_todo)
complete_btn.pack(pady=2)


listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

update_listbox()

window.mainloop()

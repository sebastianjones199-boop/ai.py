# import tkinter as tk
# from tkinter import messagebox

# expression = ""


# def press(key):
#      global expression
#      expression += str(key)
#      expression.set(expression)


# def clear():
#      global expression
#      expression = ""
#      expression.set("")


# def backspace():
#      global expression
#      expression = expression[:-1]
#      expression.set(expression)


# def calculate():
#      global expression
# try:
#          # Replace % with division by 100
#          expr = expression.replace("%", "/100")

#          result = str(eval(expr))

#          expression.set(result)
#          expression = result

# except ZeroDivisionError:
#          messagebox.showerror("Math Error", "Cannot divide by zero.")
#          expression = ""
#          expression.set("")

# except Exception:
#          messagebox.showerror("Error", "Invalid Expression")
#          expression = ""
#          expression.set("")


# def key_press(event):
#      key = event.keysym

#      if key in ("Return", "KP_Enter"):
#          calculate()

#      elif key == "BackSpace":
#          backspace()

#      elif key == "Escape":
#          clear()

#      elif event.char in "0123456789+-*/().%":
#          press(event.char)


# # # --------------------------
# # # Main Window
# # # --------------------------

# root = tk.Tk()
# root.title("Python Calculator")
# root.geometry("360x520")
# root.resizable(False, False)
# root.configure(bg="#202124")

# equation = tk.StringVar()

# display = tk.Entry()
# root,
# textvariable=equation,
# font=("Arial", 24),
# justify="right",
#     bd=10,
#     relief="sunken",
#     bg="white",
# )

# display.pack(fill="both", padx=10, pady=15, ipady=12)

# button_frame = tk.Frame(root, bg="#202124")
# button_frame.pack(expand=True, fill="both")


# def make_button(text, row, col, command, bg="#3c4043", fg="white"):
#     btn = tk.Button(
#         button_frame,
#         text=text,
#         command=command,
#         font=("Arial", 18, "bold"),
#         bg=bg,
#         fg=fg,
#         activebackground="#5f6368",
#         activeforeground="white",
#         relief="raised",
#         bd=2,
#     )

#     btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)


# # --------------------------
# # Button Layout
# # --------------------------

# buttons = [
#     ("C", 0, 0, clear, "#d93025"),
#     ("⌫", 0, 1, backspace, "#f9ab00"),
#     ("(", 0, 2, lambda: press("("), "#5f6863"),
#     (")", 0, 3, lambda: press(")"), "#5f6368"),

#     ("7", 1, 0, lambda: press("7"), "#3c4043"),
#     ("8", 1, 1, lambda: press("8"), "#3c4043"),
#     ("9", 1, 2, lambda: press("9"), "#3c4043"),
#     ("/", 1, 3, lambda: press("/"), "#4285f4"),

#     ("4", 2, 0, lambda: press("4"), "#3c4043"),
#     ("5", 2, 1, lambda: press("5"), "#3c4043"),
#     ("6", 2, 2, lambda: press("6"), "#3c4043"),
#     ("*", 2, 3, lambda: press("*"), "#4285f4"),

#     ("1", 3, 0, lambda: press("1"), "#3c4043"),
#     ("2", 3, 1, lambda: press("2"), "#3c4043"),
#     ("3", 3, 2, lambda: press("3"), "#3c4043"),
#     ("-", 3, 3, lambda: press("-"), "#4285f4"),

#     ("0", 4, 0, lambda: press("0"), "#3c4043"),
#     (".", 4, 1, lambda: press("."), "#3c4043"),
#     ("%", 4, 2, lambda: press("%"), "#3c4043"),
#     ("+", 4, 3, lambda: press("+"), "#4285f4"),
# ]

# for item in buttons:
#     make_button(*item)

# # Equals Button
# equals = tk.Button(
#     button_frame,
#     text="=",
#     command=calculate,
#     font=("Arial", 22, "bold"),
#     bg="#34a853",
#     fg="white",
#     activebackground="#2d8c46",
#     activeforeground="white",
# )

# equals.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=3, pady=3)

# # Make grid resize properly
# for i in range(6):
#     button_frame.rowconfigure(i, weight=1)

# for i in range(4):
#     button_frame.columnconfigure(i, weight=1)

# # Keyboard Support
# root.bind("<Key>", key_press)

# display.focus_set()

# # root.mainloop()

# import tkinter as tk
# from tkinter import filedialog, messagebox
# import os


# class Notepad:

#     def __init__(self, root):
#         self.root = root
#         self.filename = None

#         self.root.title("Untitled - Python Notebook")
#         self.root.geometry("900x600")

#         self.create_widgets()
#         self.create_menu()
#         self.bind_shortcuts()

#     def create_widgets(self):

#         self.text = tk.Text(
#             self.root,
#             undo=True,
#             wrap="word",
#             font=("Consolas", 12)
#         )

#         yscroll = tk.Scrollbar(self.root, command=self.text.yview)
#         self.text.configure(yscrollcommand=yscroll.set)

#         yscroll.pack(side="right", fill="y")
#         self.text.pack(fill="both", expand=True)

#         self.status = tk.Label(
#             self.root,
#             text="Line 1, Column 1",
#             anchor="w"
#         )
#         self.status.pack(fill="x")

#         self.text.bind("<KeyRelease>", self.update_status)
#         self.text.bind("<ButtonRelease>", self.update_status)

#     def create_menu(self):

#         menubar = tk.Menu(self.root)

#         filemenu = tk.Menu(menubar, tearoff=0)
#         filemenu.add_command(label="New", command=self.new_file)
#         filemenu.add_command(label="Open", command=self.open_file)
#         filemenu.add_command(label="Save", command=self.save_file)
#         filemenu.add_command(label="Save As", command=self.save_as)
#         filemenu.add_separator()
#         filemenu.add_command(label="Exit", command=self.exit_app)

#         editmenu = tk.Menu(menubar, tearoff=0)
#         editmenu.add_command(label="Undo", command=self.undo)
#         editmenu.add_command(label="Redo", command=self.redo)
#         editmenu.add_separator()
#         editmenu.add_command(label="Cut",
#                              command=lambda: self.text.event_generate("<<Cut>>"))
#         editmenu.add_command(label="Copy",
#                              command=lambda: self.text.event_generate("<<Copy>>"))
#         editmenu.add_command(label="Paste",
#                              command=lambda: self.text.event_generate("<<Paste>>"))
#         editmenu.add_separator()
#         editmenu.add_command(label="Select All",
#                              command=self.select_all)

#         viewmenu = tk.Menu(menubar, tearoff=0)

#         self.wrap_var = tk.BooleanVar(value=True)

#         viewmenu.add_checkbutton(
#             label="Word Wrap",
#             variable=self.wrap_var,
#             command=self.toggle_wrap
#         )

#         menubar.add_cascade(label="File", menu=filemenu)
#         menubar.add_cascade(label="Edit", menu=editmenu)
#         menubar.add_cascade(label="View", menu=viewmenu)

#         self.root.config(menu=menubar)

#     def bind_shortcuts(self):

#         self.root.bind("<Control-n>", lambda e: self.new_file())
#         self.root.bind("<Control-o>", lambda e: self.open_file())
#         self.root.bind("<Control-s>", lambda e: self.save_file())
#         self.root.bind("<Control-z>", lambda e: self.undo())
#         self.root.bind("<Control-y>", lambda e: self.redo())
#         self.root.bind("<Control-a>", lambda e: self.select_all())

#         self.root.protocol("WM_DELETE_WINDOW", self.exit_app)

#     def update_title(self):

#         if self.filename:
#             name = os.path.basename(self.filename)
#         else:
#             name = "Untitled"

#         self.root.title(f"{name} - Python Notebook")

#     def new_file(self):

#         if not self.confirm_save():
#             return

#         self.text.delete("1.0", "end")
#         self.text.edit_reset()
#         self.text.edit_modified(False)

#         self.filename = None
#         self.update_title()

#     def open_file(self):

#         if not self.confirm_save():
#             return

#         filename = filedialog.askopenfilename(
#             filetypes=[
#                 ("Text Files", "*.txt"),
#                 ("Python Files", "*.py"),
#                 ("All Files", "*.*")
#             ]
#         )

#         if not filename:
#             return

#         try:
#             with open(filename, "r", encoding="utf-8") as file:
#                 text = file.read()

#             self.text.delete("1.0", "end")
#             self.text.insert("1.0", text)

#             self.filename = filename
#             self.text.edit_reset()
#             self.text.edit_modified(False)

#             self.update_title()

#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def save_file(self):

#         if self.filename is None:
#             return self.save_as()

#         try:
#             with open(self.filename, "w", encoding="utf-8") as file:
#                 file.write(self.text.get("1.0", "end-1c"))

#             self.text.edit_modified(False)

#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def save_as(self):

#         filename = filedialog.asksaveasfilename(
#             defaultextension=".txt",
#             filetypes=[
#                 ("Text Files", "*.txt"),
#                 ("Python Files", "*.py"),
#                 ("All Files", "*.*")
#             ]
#         )

#         if filename:
#             self.filename = filename
#             self.save_file()
#             self.update_title()

#     def confirm_save(self):

#         if not self.text.edit_modified():
#             return True

#         answer = messagebox.askyesnocancel(
#             "Save Changes",
#             "Do you want to save your changes?"
#         )

#         if answer is None:
#             return False

#         if answer:
#             self.save_file()

#         return True

#     def exit_app(self):

#         if self.confirm_save():
#             self.root.destroy()

#     def undo(self):

#         try:
#             self.text.edit_undo()
#         except tk.TclError:
#             pass

#     def redo(self):

#         try:
#             self.text.edit_redo()
#         except tk.TclError:
#             pass

#     def select_all(self):

#         self.text.tag_add("sel", "1.0", "end")
#         return "break"

#     def toggle_wrap(self):

#         self.text.config(
#             wrap="word" if self.wrap_var.get() else "none"
#         )

#     def update_status(self, event=None):

#         line, column = self.text.index("insert").split(".")
#         self.status.config(
#             text=f"Line {line}, Column {int(column)+1}"
#         )


# def main():

#     root = tk.Tk()
#     Notepad(root)
#     root.mainloop()

for i in range (100):
      print(i)
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

Version='1.2.3.4'
Default="D:\\"

def ask_question():
    question = "Click browse to change default installation directory"

    # Create styled dialog box
    dialog = tk.Toplevel()
    dialog.title("Installing Everest "+Version)
    dialog.resizable(True,True)
    style = ttk.Style(dialog)
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TButton', font=('Helvetica', 10))
    
    question_label = ttk.Label(dialog, text=question, padding=(40, 20, 10, 0), anchor="center")
    question_label.pack(fill='x')

    submit_button = ttk.Button(dialog, text="Browse", command=dialog.destroy)
    submit_button.pack(pady=10)

    submit_button = ttk.Button(dialog, text="Install", command=dialog.destroy)
    submit_button.pack(pady=10)

    ok_button = ttk.Button(dialog, text="Install", command=submit_button)
    ok_button.bind("<<Button>>", lambda event: ok_cancel_clicked.set("Install"))
    ok_cancel_clicked = tk.StringVar(value="Install")

    # Add the input field
    answer = tk.StringVar(value="D:\\")
    answer_entry = ttk.Entry(dialog, textvariable=answer, font=('Helvetica', 14))
    answer_entry.pack(fill='x', padx=10, pady=10)

    # Center the dialog box on the screen
    dialog.update_idletasks()
    screen_width = dialog.winfo_screenwidth()
    screen_height = dialog.winfo_screenheight()
    dialog_width = dialog.winfo_width()
    dialog_height = dialog.winfo_height()
    x = (screen_width // 2) - (dialog_width // 2)
    y = (screen_height // 2) - (dialog_height // 2)
    dialog.geometry('{}x{}+{}+{}'.format(dialog_width, dialog_height, x, y))

    # Focus the input field
    answer_entry.focus_set()

    # Wait for the user to input their answer
    dialog.wait_window()
    
    # Return the user's answer
    ans = answer.get()

    if ok_cancel_clicked.get() == "Install":
       print("User clicked OK button")
       return Default

    if ans != Default:
       return answer.get()
    else:
       return Default

# Example usage
if ask_question() == Default:
   dir_path = Default
else:
   # ask the user to select a file using the file dialog
   options = {
      "title": "Select a folder",
      "initialdir": "/",
   }
   # ask the user to select a directory using the folder selection dialog
   dir_path = filedialog.askdirectory(**options)

print("Selected directory:", dir_path)



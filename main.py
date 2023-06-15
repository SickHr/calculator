import tkinter as tk
from tkinter import Entry, Button

# Function to execute when a button is pressed
def on_button_press(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("260x310")
root.resizable(0, 0)  # Make the window non-resizable

# Entry widget for user input
entry = Entry(root, width=16, font=("Arial", 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons and their corresponding text
buttons_text = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3), ('=', 4, 2),
    ('C', 4, 0)
]

# Create buttons and add them to the main window
for button_text, row, column in buttons_text:
    button = Button(root, text=button_text, width=5, height=2, font=("Arial", 13),
                    bg='#f2f2f2', command=lambda b=button_text: on_button_press(b))
    button.grid(row=row, column=column, padx=5, pady=5)

# Start the main event loop
root.mainloop()
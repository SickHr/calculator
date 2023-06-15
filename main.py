import customtkinter as ctk

# Root window
root = ctk.CTk()
root.title("Calculator")
root.geometry("345x350")
root.resizable(False, False)


def on_button_press(button_text):
    current_text = entry1.get()
    if button_text == "=":

        eval(current_text)
        result = eval(current_text)
        entry1.delete(0, "end")
        entry1.insert("end", result)

    elif button_text == "c":
        entry1.delete(0, "end")
    else:
        entry1.delete(0, "end")
        entry1.insert("end", current_text + button_text)


# entry
entry1 = ctk.CTkEntry(root, width=200, font=("Arial", 20))
entry1.grid(column=0, row=0, columnspan=5, padx=51, pady=51)

# Display
buttons_position = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("c", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("+", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("*", 4, 3)

]

for text, row, column in buttons_position:
    button = ctk.CTkButton(root, text=text, width=75, height=40, font=("Arial", 20), command=lambda text=text: on_button_press(text))
    button.grid(column=column, row=row, padx=5, pady=5)

if __name__ == '__main__':
    root.mainloop()

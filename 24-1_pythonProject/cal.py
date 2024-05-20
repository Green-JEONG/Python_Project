import tkinter as tk

# Function to update the expression in the entry box
def update_expression(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Set the background color of the main window
root.configure(bg='light green')

# Create the entry box with green background
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2, justify='right', bg='pale green')
entry.grid(row=0, column=0, columnspan=4)

# Define the button texts and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 4)  # Clear button spanning across 4 columns
]

# Create the buttons and place them in the grid with green theme
for (text, row, col, *span) in buttons:
    colspan = span[0] if span else 1
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), bg='green', fg='white', command=calculate).grid(row=row, column=col, columnspan=colspan, sticky="nsew")
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), bg='dark green', fg='white', command=clear).grid(row=row, column=col, columnspan=colspan, sticky="nsew")
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), bg='light green', fg='black', command=lambda b=text: update_expression(b)).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

# Configure row and column weights to make buttons resize with window
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()

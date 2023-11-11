
import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("Basic Calculator")
app.configure(bg="light gray")  # Set background color

# Create a text input field for the calculator display
display = tk.Entry(app, width=20, font=('Helvetica', 24))
display.grid(row=0, column=0, columnspan=4)

# Function to update the display when buttons are pressed
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to perform arithmetic operations
def calculate():
    try:
        expression = display.get()
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Customize button appearance
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row_index = 1
col_index = 0

for button_text in button_texts:
    if button_text == "C":
        button = tk.Button(app, text=button_text, padx=30, pady=30, font=('Arial', 20), command=clear_display, bg="red", fg="white")
    elif button_text == "=":
        button = tk.Button(app, text=button_text, padx=30, pady=30, font=('Arial', 20), command=calculate, bg="yellow", fg="black")
    else:
        button = tk.Button(app, text=button_text, padx=30, pady=30, font=('Arial', 20), command=lambda text=button_text: button_click(text), bg="blue", fg="white")
    button.grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

# Start the main loop
app.mainloop()


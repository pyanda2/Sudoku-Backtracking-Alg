from operator import truediv
import tkinter as tk

GRID_LEN = 9

# Create window, starting screen
window = tk.Tk()
window.title("Sudoku")
window.geometry('300x500')

test = tk.Label(window, text="Welcome to sudoku!", bg="#ed9f40", fg="black")
test.pack(side=tk.TOP, pady=50)
test = tk.Label(window, text="Green", bg="green", fg="white")
test.pack(side=tk.TOP, pady=50)
test = tk.Label(window, text="Purple", bg="purple", fg="white")
test.pack(side=tk.TOP, pady=50)


def start_game():
    def b_click(butt): # button clicked function
        butt.config(bg="blue", text="h")
        pass

    # dynamically create variable name
    # Create 9x9 square buttons
    def callback(input):
        if (len(input) < 2 and input.isdigit()) or (input == ""):
            return True
        return False
    reg=window.register(callback)
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            val = tk.Entry(window, validate="key", font=("Times", 10), width=2, bg="orange", validatecommand=(reg, '%P'), justify="center")
            val.grid(row=i, column=j)

window.mainloop()

# sources:
# https://www.geeksforgeeks.org/python-tkinter-validating-entry-widget/
import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        if operation.get() == "Square Root":
            if num1 < 0:
                result_label.config(text="Error: Negative number")
                return
            result = num1 ** 0.5
        else:
            num2 = float(entry2.get())
            if not (operation.get() in ["Add", "Subtract", "Multiply", "Divide"]):
                result_label.config(text="Error: Invalid operation")
                return
            if operation.get() == "Add":
                result = num1 + num2
            elif operation.get() == "Subtract":
                result = num1 - num2
            elif operation.get() == "Multiply":
                result = num1 * num2
            elif operation.get() == "Divide":
                if num2 == 0:
                    result_label.config(text="Error: Division by zero")
                    return
                result = num1 / num2
        result_label.config(text=str(result))
    except ValueError:
        result_label.config(text="Error: Invalid input")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Simple Calculator")

frame = tk.Frame(root)
frame.pack()

label1 = tk.Label(frame, text="Number 1:", font=("Arial", 16))
label1.pack(side=tk.LEFT)

entry1 = tk.Entry(frame, font=("Arial", 16))
entry1.pack(side=tk.LEFT)

label2 = tk.Label(frame, text="Number 2:", font=("Arial", 16))
label2.pack(side=tk.LEFT)

entry2 = tk.Entry(frame, font=("Arial", 16))
entry2.pack(side=tk.LEFT)

label3 = tk.Label(frame, text="Operation:", font=("Arial", 16))
label3.pack(side=tk.LEFT)

operation = tk.StringVar()
operation_choices = tk.OptionMenu(frame, operation, "Add", "Subtract", "Multiply", "Divide", "Square Root")
operation_choices.pack(side=tk.LEFT)

calculate_button = tk.Button(frame, text="Calculate", font=("Arial", 16), command=calculate)
calculate_button.pack(side=tk.LEFT)

clear_button = tk.Button(frame, text="Clear", font=("Arial", 16), command=clear)
clear_button.pack(side=tk.LEFT)

result_label = tk.Label(frame, text="", font=("Arial", 16))
result_label.pack(side=tk.LEFT)

root.mainloop()

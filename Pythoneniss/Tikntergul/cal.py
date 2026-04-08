import tkinter as tk

def add():
    n1 = int(e1.get())
    n2 = int(e2.get())
    result = n1 + n2
    label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Addition")
root.geometry("300x200")

# Input fields
e1 = tk.Entry(root)
e1.pack()

e2 = tk.Entry(root)
e2.pack()

# Button
btn = tk.Button(root, text="Add", command=add)
btn.pack()

# Result
label = tk.Label(root, text="")
label.pack()

root.mainloop()
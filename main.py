import tkinter as tk


# Window
root = tk.Tk()
root.title("Starter Level Calculator")
root.geometry("275x540+250+250")
root.resizable(False, False)


# Lists
numberList = []

# Functions
def buttonClick(number):
    current = e.get()
    e.delete(0, "end")
    e.insert(0, str(current) + str(number))

def equal():
    b = e.get()
    numberList.append(b)
    c = (int(numberList[0]) + int(numberList[1]))
    e.delete(0, "end")
    e.insert(0,c)
    numberList.clear()

def plus():
    a = e.get()
    numberList.append(a)
    e.delete(0, "end")

def clear():
    e.delete(0, "end")


# Number Entry Button
e = tk.Entry(root, width=40, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Defining Buttons
button1 = tk.Button(root, text="1", fg="white", bg="gray", activebackground="red",padx=30, pady=30, command=lambda: buttonClick(1))

button2 = tk.Button(root, text="2", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=lambda: buttonClick(2))

button3 = tk.Button(root, text="3", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=lambda: buttonClick(3))

button4 = tk.Button(root, text="4", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=lambda: buttonClick(4))

button5 = tk.Button(root, text="5", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=lambda: buttonClick(5))

button6 = tk.Button(root, text="6", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=lambda: buttonClick(6))

button7 = tk.Button(root, text="7", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=lambda: buttonClick(7))

button8 = tk.Button(root, text="8", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=lambda: buttonClick(8))

button9 = tk.Button(root, text="9", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=lambda: buttonClick(9))

button10 = tk.Button(root, text="0", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=lambda: buttonClick(0))

buttonEqual = tk.Button(root, text="=", fg="white", bg="gray", activebackground="red", padx=75, pady=30, command=equal)

buttonPlus = tk.Button(root, text="+", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=plus)

buttonClear = tk.Button(root, text="Clear", fg="white", bg="gray", activebackground="red", padx=65, pady=30, command=clear)

# Putting Buttons On The Screen
button1.place(x=190, y=250)
button2.place(x=100, y=250)
button3.place(x=10, y=250)

button4.place(x=190, y=150)
button5.place(x=100, y=150)
button6.place(x=10, y=150)

button7.place(x=10, y=50)
button8.place(x=100, y=50)
button9.place(x=190, y=50)


button10.place(x=10, y=350)

buttonClear.place(x=100, y=350)

buttonPlus.place(x=10, y=450)

buttonEqual.place(x=100, y=450)

root.mainloop()

print(numberList)


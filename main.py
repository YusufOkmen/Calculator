import tkinter as tk


# Window
root = tk.Tk()
root.title("Starter Level Calculator")
root.geometry("380x560+250+250")
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
    if "+" in numberList:
        c = (int(numberList[0]) + int(numberList[2])) # we are using index 0 and 2. It is because we first take first value than operator(+,-,*,%) and finally the second value in our list.
        e.delete(0, "end")
        e.insert(0,c)
        numberList.clear()
    elif "-" in numberList:
        c = (int(numberList[0]) - int(numberList[2]))
        e.delete(0, "end")
        e.insert(0,c)
        numberList.clear()
    elif "*" in numberList:
        c = (int(numberList[0]) * int(numberList[2]))
        e.delete(0, "end")
        e.insert(0,c)
        numberList.clear()
    elif "%" in numberList:
        c = round((int(numberList[0]) / int(numberList[2])))
        e.delete(0, "end")
        e.insert(0,c)
        numberList.clear()
    elif "**" in numberList:
        c = round((int(numberList[0]) ** int(numberList[2])))
        e.delete(0, "end")
        e.insert(0,c)
        numberList.clear()

def plus():
    a = e.get()
    numberList.append(a)
    numberList.append("+")
    e.delete(0, "end")

def divide():
    a = e.get()
    numberList.append(a)
    numberList.append("%")
    e.delete(0, "end")

def multi():
    a = e.get()
    numberList.append(a)
    numberList.append("*")
    e.delete(0, "end")

def minus():
    a = e.get()
    numberList.append(a)
    numberList.append("-")
    e.delete(0, "end")

def square():
    a = e.get()
    numberList.append(a)
    numberList.append("**")
    e.delete(0, "end")

def clear():
    e.delete(0, "end")
    numberList.clear()


# Number Entry Button
e = tk.Entry(root, width=57, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Defining Buttons

button1 = tk.Button(root, text="1", fg="white", bg="gray", activebackground="pink",padx=30, pady=30, command=lambda: buttonClick(1), borderwidth=10)

button2 = tk.Button(root, text="2", fg="white", bg="gray", activebackground="red", padx=30, pady=30, command=lambda: buttonClick(2), borderwidth=10)

button3 = tk.Button(root, text="3", fg="white", bg="gray", activebackground="blue", padx=30, pady=30, command=lambda: buttonClick(3), borderwidth=10)

button4 = tk.Button(root, text="4", fg="white", bg="gray", activebackground="orange", padx=30, pady=30, command=lambda: buttonClick(4), borderwidth=10)

button5 = tk.Button(root, text="5", fg="white", bg="gray", activebackground="brown", padx=30, pady=30, command=lambda: buttonClick(5), borderwidth=10)

button6 = tk.Button(root, text="6", fg="white", bg="gray", activebackground="black", padx=30, pady=30, command=lambda: buttonClick(6), borderwidth=10)

button7 = tk.Button(root, text="7", fg="white", bg="gray", activebackground="white", padx=30, pady=30, command=lambda: buttonClick(7), borderwidth=10)

button8 = tk.Button(root, text="8", fg="white", bg="gray", activebackground="yellow", padx=30, pady=30, command=lambda: buttonClick(8), borderwidth=10)

button9 = tk.Button(root, text="9", fg="white", bg="gray", activebackground="green", padx=30, pady=30, command=lambda: buttonClick(9), borderwidth=10)

button10 = tk.Button(root, text="0", fg="white", bg="gray", activebackground="purple", padx=30, pady=30, command=lambda: buttonClick(0), borderwidth=10)

buttonEqual = tk.Button(root, text="=", fg="white", bg="brown", activebackground="red", padx=120, pady=30, command=equal, borderwidth=10)

buttonClear = tk.Button(root, text="Clear", fg="white", bg="brown", activebackground="red", padx=65, pady=30, command=clear, borderwidth=10)

buttonPlus = tk.Button(root, text="+", fg="white", bg="brown", activebackground="red", padx=30, pady=30, command=plus, borderwidth=10)

buttonDivide = tk.Button(root, text="%", fg="white", bg="brown", activebackground="red", padx=30, pady=30, command=divide, borderwidth=10)

buttonMulti = tk.Button(root, text="*", fg="white", bg="brown", activebackground="red", padx=32, pady=30, command=multi, borderwidth=10)

buttonMinus = tk.Button(root, text="-", fg="white", bg="brown", activebackground="red", padx=32, pady=30, command=minus, borderwidth=10)

buttonSquare = tk.Button(root, text="**", fg="white", bg="brown", activebackground="red", padx=30, pady=30, command=square, borderwidth=10)


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

buttonPlus.place(x=280, y=50)

buttonMinus.place(x=280, y=150)

buttonDivide.place(x=280, y=250)

buttonMulti.place(x=280, y=350)

buttonSquare.place(x=280, y=450)

buttonEqual.place(x=10, y=450)

root.mainloop()

print(numberList)


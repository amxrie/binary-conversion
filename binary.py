from tkinter import *
from tkinter import messagebox


def number_to_binary(number):
    number = int(number)
    binary = []
    while number != 0:
        binary.insert(0, number % 2)
        number //= 2
    return binary


def binary_to_number(bytecode):
    n = len(bytecode)
    byte = []
    binary = []
    number = []
    for bit in bytecode:
        byte.insert(0, int(bit))
    for exp in range(n):
        binary.append(2**exp)
    for i in range(n):
        number.append(byte[i] * binary[i])
    return sum(number)


def clear_entry():
    binary_entry.delete(0, END)
    decimal_entry.delete(0, END)
    alphabet_entry.delete(0, END)


def convert():
    if binary_entry.get():
        binary_code = binary_entry.get()
        alphabet_entry.insert(0, chr(binary_to_number(binary_code)))
        decimal_entry.insert(0, str(binary_to_number(binary_code)))
    elif decimal_entry.get():
        decimal = decimal_entry.get()
        binary = ""
        for bit in number_to_binary(decimal):
            binary += str(bit)
        binary_entry.insert(0, binary)
        alphabet_entry.insert(0, chr(int(decimal)))
    elif alphabet_entry.get():
        alphabet = alphabet_entry.get()
        binary = ""
        for bit in number_to_binary(ord(alphabet)):
            binary += str(bit)
        binary_entry.insert(0, binary)
        decimal_entry.insert(0, str(ord(alphabet)))


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


def on_closing():
    messagebox.showinfo("About", "Programmer: amxrie")
    window.destroy()


window = Tk()
window.title("Conversion")
window.geometry("250x170")
center_window(window)

label_texts = ["Binary Number:", "Decimal Number:", "Alphabet Letter:"]
labels = {}
for i, text in enumerate(label_texts):
    labels[f"{text}"] = Label(window, text=text, justify=RIGHT)
    labels[f"{text}"].grid(row=i+1, column=0, padx=5, pady=5, sticky=W)

entries = {"column": "1", "padx": "5", "pady": "5", "sticky": "E"}
window.columnconfigure(1, weight=3)

binary_entry = Entry(window)
binary_entry.grid(row=1, **entries)

decimal_entry = Entry(window)
decimal_entry.grid(row=2, **entries)

alphabet_entry = Entry(window)
alphabet_entry.grid(row=3, **entries)

buttons = {"column": "0", "columnspan": "2", "padx": "5", "pady": "5", "ipadx": "100"}

convert_button = Button(window, text="Convert", command=convert)
convert_button.grid(row=4, **buttons)

clear_button = Button(window, text="Clear", command=clear_entry)
clear_button.grid(row=5, **buttons)

window.bind("<Return>", lambda event: convert_button.invoke())

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()

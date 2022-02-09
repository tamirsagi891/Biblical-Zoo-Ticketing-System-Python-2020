import tkinter as tk
from tkinter import filedialog, Text, ttk, Label
from main import *
from PIL import Image, ImageTk


def send_code(event=None):
    code = textBox.get("1.0", "end-1c")
    code = code.strip()
    outcome = get_ticket(code)
    if outcome != '1':
        screen['text'] = outcome
        textBox.delete("1.0", "end")
    else:
        screen['text'] = 'הכנס קוד'
        textBox.delete("1.0", "end")


def clear_code():
    textBox.delete("1.0", "end")


def delete_num():
    code = textBox.get("1.0", "end-1c")
    if len(code) > 0:
        code = code[:-1]
        textBox.delete("1.0", "end")
        textBox.insert("1.0", code)


func_arr = []

for i in range(10):
    def f(i = i):
        textBox.insert("end", str(i))

    func_arr.append(f)


root = tk.Tk()
root.title('גן החיות התנכי')
root.resizable(width=False, height=False)

canvas = tk.Canvas(root, heigh=669, width=455) # 450
canvas.pack()

frame = tk.Frame(root, bg='green4')
frame.place(relwidth=1, relheight=1)

screen = Label(frame, text='הכנס קוד', bg='green4', font="Times 20 bold")
screen.grid(column=0, row=1,  padx=5, pady=5, columnspan=4)

textBox = Text(frame, height=1, width=35, padx=10, pady=5, font="Times 14 bold")
textBox.grid(column=0, row=2, padx=5, pady=5, columnspan=4)

submit_button = tk.Button(frame, text="שלח קוד", command=send_code, pady=3, padx=100, font="Times 14 bold")
submit_button.grid(column=0, row=3, pady=5, columnspan=4)

image1 = Image.open('im1.jpg')
image1 = image1.resize((450, 250), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(frame, image=test)
label1.image = test

label1.grid(column=0, row=8, pady=5, columnspan=4)


num1 = tk.Button(frame, text="1", command=func_arr[1], pady=15, padx=64, font="Times 14 bold")
num1.grid(column=0, row=4, pady=0, sticky='E')

num2 = tk.Button(frame, text="2", command=func_arr[2], pady=15, padx=64, font="Times 14 bold")
num2.grid(column=1, row=4, pady=0)

num3 = tk.Button(frame, text="3", command=func_arr[3], pady=15, padx=64, font="Times 14 bold")
num3.grid(column=2, row=4, pady=0, sticky='W')

num4 = tk.Button(frame, text="4", command=func_arr[4], pady=15, padx=64, font="Times 14 bold")
num4.grid(column=0, row=5, pady=0, sticky='E')

num5 = tk.Button(frame, text="5", command=func_arr[5], pady=15, padx=64, font="Times 14 bold")
num5.grid(column=1, row=5, pady=0)

num6 = tk.Button(frame, text="6", command=func_arr[6], pady=15, padx=64, font="Times 14 bold")
num6.grid(column=2, row=5, pady=0, sticky='W')

num7 = tk.Button(frame, text="7", command=func_arr[7], pady=15, padx=64, font="Times 14 bold")
num7.grid(column=0, row=6, pady=0, sticky='E')

num8 = tk.Button(frame, text="8", command=func_arr[8], pady=15, padx=64, font="Times 14 bold")
num8.grid(column=1, row=6, pady=0)

num9 = tk.Button(frame, text="9", command=func_arr[9], pady=15, padx=64, font="Times 14 bold")
num9.grid(column=2, row=6, pady=0, sticky='W')

del_button = tk.Button(frame, text="DEL", command=delete_num, pady=15, padx=49, font="Times 14 bold")
del_button.grid(column=0, row=7, pady=0, sticky='E')

num0 = tk.Button(frame, text="0", command=func_arr[0], pady=15, padx=64, font="Times 14 bold")
num0.grid(column=1, row=7, pady=0)

clear_button = tk.Button(frame, text="CLEAR", command=clear_code, pady=15, padx=35, font="Times 14 bold")
clear_button.grid(column=2, row=7, pady=0, sticky='W')

root.bind("<Return>", send_code)
root.mainloop()

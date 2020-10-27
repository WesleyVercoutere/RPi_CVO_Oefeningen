from tkinter import *

root = Tk()
root.title("Hello World")
root.geometry("800x400")

label1 = Label(root, text="Hello World!")
label1.place(x=10, y=10)

def changeColor():
    label1["bg"]="red"

btn = Button(root, text="Click", command=changeColor)
btn.place(x=10, y=50)


def changePlace():
    label1.place(x=50, y=10)

btn2 = Button(root, text="Move", command=changePlace)
btn2.place(x=10, y=100)


entry = Entry(root)
entry.place(x=10, y=200)

def getText():
    label2 = Label(root, text=entry.get())
    label2.pack()

btn3 = Button(root, text="get text", command=getText)
btn3.place(x=10, y=250)

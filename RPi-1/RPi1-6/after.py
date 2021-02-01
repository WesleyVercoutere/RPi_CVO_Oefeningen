from tkinter import *
import threading
import time

root = Tk()
root.title("Test after method")
root.geometry("800x400")

LOOP_TIME = 1 # 1s
counter = 0

label1 = Label(root, text=counter)
label1.place(x=10, y=10)

def update_label():
    global counter
    start_time = time.time()

    while True:
        current_time = time.time()
        
        if current_time >= start_time + LOOP_TIME:
            counter += 1
            label1['text'] = counter
            start_time = time.time()
            print(start_time)
    

threading.Thread(target=update_label).start()

root.mainloop()

#test git

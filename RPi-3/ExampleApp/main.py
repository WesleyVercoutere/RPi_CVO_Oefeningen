from tkinter import *


class Main:

    def __init__(self):
        self.root = Tk()
        self.root.title("Example App")
        self.root.geometry("800x400")

        self.persons = ["Marcel Kiekeboe", "Charlotte Kiekeboe", "Fanny Kiekeboe", "Konstantinopel Kiekeboe"]

        self.showPersons()

        self.root.mainloop()

    def showPersons(self):
        row = 0
        column = 0

        for person in self.persons:
            label = Label(self.root, text=person)
            label.grid(column=column, row=row)
            row += 1


if __name__ == '__main__':
    Main()
    # of
    # main = Main()

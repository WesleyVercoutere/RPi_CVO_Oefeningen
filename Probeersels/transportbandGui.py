import time
from tkinter import *


class DesktopGUI:

    def __init__(self):
        self.root = None
        self.setupRoot()

        self.currentState = StringVar()
        self.currentState.set("Test")
        self.currentPosition = StringVar()
        self.currentPosition.set("Test")
        self.currentSteps = IntVar()
        self.currentSteps.set(999)
        self.currentMessage = StringVar()
        self.currentMessage.set("Very long ............................................. text")

        self.setupStateSection()
        self.setupControlSection()
        self.setupSettingsSection()

        self.loop()

    def setupRoot(self):
        self.root = Tk()
        self.root.title('Transportband')

        self.root.columnconfigure(0, weight=1)

    def setupStateSection(self):
        frame = LabelFrame(self.root, text = "Conveyor State", padx=10, pady=10)

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        frame1 = Frame(frame)
        lbl_state = Label(frame1, text="State : ")
        lbl_state.grid(column=0, row=0)
        lbl_currentState = Label(frame1, textvariable=self.currentState, fg="blue")
        lbl_currentState.grid(column=1, row=0)
        frame1.grid(column=0, row=0, sticky="w", padx=10, pady=5)

        frame2 = Frame(frame)
        lbl_position = Label(frame2, text="Position : ")
        lbl_position.grid(column=0, row=0)
        lbl_currentState = Label(frame2, textvariable=self.currentPosition, fg="blue")
        lbl_currentState.grid(column=1, row=0)
        frame2.grid(column=1, row=0, sticky="w", padx=10, pady=5)

        frame3 = Frame(frame)
        lbl_steps = Label(frame3, text="Nbr of steps from home position : ")
        lbl_steps.grid(column=0, row=0)
        lbl_currentSteps = Label(frame3, textvariable=self.currentSteps, fg="blue")
        lbl_currentSteps.grid(column=1, row=0)
        frame3.grid(column=2, row=0, sticky="w", padx=10, pady=5)

        frame4 = Frame(frame)
        lbl_state = Label(frame4, text="Message : ")
        lbl_state.grid(column=0, row=0)
        lbl_currentMessage = Label(frame4, textvariable=self.currentMessage, fg="blue")
        lbl_currentMessage.grid(column=1, row=0)
        frame4.grid(column=0, row=1, sticky="w", padx=10, pady=5, columnspan=3)

        frame.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

    def setupControlSection(self):
        frame = LabelFrame(self.root, text = "Conveyor Control", padx=10, pady=10)

        for i in range(5):
            frame.columnconfigure(i, weight=1)

        btn_home = Button(frame, text="Home")
        btn_home.grid(column=0, row=0, padx=10, pady=10, sticky='ew')
        btn_stepLeft = Button(frame, text="<- 1")
        btn_stepLeft.grid(column=1, row=0, padx=10, pady=10, sticky='ew')
        btn_pos1 = Button(frame, text="Position 1")
        btn_pos1.grid(column=2, row=0, padx=10, pady=10, sticky='ew')
        btn_pos2 = Button(frame, text="Position 2")
        btn_pos2.grid(column=3, row=0, padx=10, pady=10, sticky='ew')
        btn_stepRight = Button(frame, text="1 ->")
        btn_stepRight.grid(column=4, row=0, padx=10, pady=10, sticky='ew')

        frame.grid(column=0, row=1, padx=10, pady=10, sticky='ew')

    def setupSettingsSection(self):
        frame = LabelFrame(self.root, text = "Conveyor Settings", padx=10, pady=10)

        lbl_state = Label(frame, text="Position 1 : ")
        lbl_state.grid(column=0, row=0, sticky="w", padx=10, pady=5)
        lbl_position = Label(frame, text="Position 2 : ")
        lbl_position.grid(column=0, row=1, sticky="w", padx=10, pady=5)

        frame.grid(column=0, row=2, padx=10, pady=10, sticky='ew')


    def update(self, *args, **kwargs):
        message = kwargs["message"]

    def loop(self):
        self.root.mainloop()


if __name__ == "__main__":
    DesktopGUI()
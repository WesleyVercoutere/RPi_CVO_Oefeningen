from tkinter import *

from hardware import Rotation as Rotation
from util.observer.Observer import Observer
from util import PositionState as PositionState

"""
https://www.dreamincode.net/forums/topic/371440-tkinter-overview-with-a-fixed-width-grid/
"""
class DesktopGUI(Observer):

    def __init__(self, conveyorManager, desktopController):
        self.mgr = conveyorManager
        self.mgr.addObserver(self)
        self.controller = desktopController

        self.root = None
        self.setupRoot()

        self.currentState = StringVar()
        self.currentPosition = StringVar()
        self.currentSteps = IntVar()
        self.currentMessage = StringVar()

        self.setupStateSection()
        self.setupControlSection()
        self.setupSettingsSection()

    def setupRoot(self):
        self.root = Tk()
        self.root.title('Transportband')
        self.root.geometry("800x400")
        self.root.resizable(width=False, height=True)
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
        frame1.grid(column=0, row=0, sticky="ew", padx=10, pady=5)

        frame2 = Frame(frame)
        lbl_position = Label(frame2, text="Position : ")
        lbl_position.grid(column=0, row=0)
        lbl_currentState = Label(frame2, textvariable=self.currentPosition, fg="blue")
        lbl_currentState.grid(column=1, row=0)
        frame2.grid(column=1, row=0, sticky="ew", padx=10, pady=5)

        frame3 = Frame(frame)
        lbl_steps = Label(frame3, text="Nbr of steps from home position : ")
        lbl_steps.grid(column=0, row=0)
        lbl_currentSteps = Label(frame3, textvariable=self.currentSteps, fg="blue")
        lbl_currentSteps.grid(column=1, row=0)
        frame3.grid(column=2, row=0, sticky="ew", padx=10, pady=5)

        frame4 = Frame(frame)
        lbl_state = Label(frame4, text="Message : ")
        lbl_state.grid(column=0, row=0)
        lbl_currentMessage = Label(frame4, textvariable=self.currentMessage, fg="blue")
        lbl_currentMessage.grid(column=1, row=0)
        frame4.grid(column=0, row=1, sticky="ew", padx=10, pady=5, columnspan=3)

        frame.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

    def setupControlSection(self):
        frame = LabelFrame(self.root, text = "Conveyor Control", padx=10, pady=10)

        for i in range(5):
            frame.columnconfigure(i, weight=1)

        btn_home = Button(frame, text="Home", command=lambda: self.controller.btnMoveToPosition_clicked(PositionState.HOME))
        btn_home.grid(column=0, row=0, padx=10, pady=10, sticky='ew')
        btn_stepLeft = Button(frame, text="<- 1", command=lambda: self.controller.btnMoveOneStep_clicked(Rotation.COUNTERCLOCKWISE))
        btn_stepLeft.grid(column=1, row=0, padx=10, pady=10, sticky='ew')
        btn_pos1 = Button(frame, text="Position 1", command=lambda: self.controller.btnMoveToPosition_clicked(PositionState.POSITION_1))
        btn_pos1.grid(column=2, row=0, padx=10, pady=10, sticky='ew')
        btn_pos2 = Button(frame, text="Position 2", command=lambda: self.controller.btnMoveToPosition_clicked(PositionState.POSITION_2))
        btn_pos2.grid(column=3, row=0, padx=10, pady=10, sticky='ew')
        btn_stepRight = Button(frame, text="1 ->", command=lambda: self.controller.btnMoveOneStep_clicked(Rotation.CLOCKWISE))
        btn_stepRight.grid(column=4, row=0, padx=10, pady=10, sticky='ew')

        frame.grid(column=0, row=1, padx=10, pady=10, sticky='ew')

    def setupSettingsSection(self):
        frame = LabelFrame(self.root, text = "Conveyor Settings", padx=10, pady=10)

        frame1 = Frame(frame)
        lbl_state = Label(frame1, text="Position 1 : ")
        lbl_state.grid(column=0, row=0, sticky="w", padx=10, pady=5)
        lbl1 = Label(frame1, text="ToDo", fg='red')
        lbl1.grid(column=1, row=0)
        frame1.grid(column=0, row=0, sticky="ew", padx=10, pady=5)

        frame2 = Frame(frame)
        lbl_position = Label(frame2, text="Position 2 : ")
        lbl_position.grid(column=0, row=1, sticky="w", padx=10, pady=5)
        lbl2 = Label(frame2, text="ToDo", fg='red')
        lbl2.grid(column=1, row=1)
        frame2.grid(column=0, row=1, sticky="ew", padx=10, pady=5)

        frame.grid(column=0, row=2, padx=10, pady=10, sticky='ew')

    def update(self, *args, **kwargs):
        message = kwargs["message"]

        dto = self.mgr.getState()

        self.currentState.set(dto.state)
        self.currentPosition.set(dto.position)
        self.currentSteps.set(dto.steps)
        self.currentMessage.set(message)

    def loop(self):
        self.root.mainloop()

import RPi.GPIO as GPIO
import json
import time
from tkinter import *

class Domotica:

    def __init__(self):
        self.setIO()
        self.setCallbacks()
        self.initSettings()

        self.setRoot()
        self.loadSettings()

        self.runLoop()

    def setIO(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.pinBtn1 = 5
        self.pinBtn2 = 6
        self.pinBtn3 = 13
        self.buttons = (self.pinBtn1, self.pinBtn2, self.pinBtn3)

        self.pinRed = 16
        self.pinGreen = 20
        self.pinBlue = 21
        self.leds = (self.pinRed, self.pinGreen, self.pinBlue)

        GPIO.setup(self.buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self.leds, GPIO.OUT)
        GPIO.output(self.leds, GPIO.LOW)

    def setCallbacks(self):
        GPIO.add_event_detect(self.pinBtn1, GPIO.RISING, callback = self.toggle, bouncetime = 200)
        GPIO.add_event_detect(self.pinBtn2, GPIO.RISING, callback = self.toggle, bouncetime = 200)
        GPIO.add_event_detect(self.pinBtn3, GPIO.RISING, callback = self.toggle, bouncetime = 200)

    def toggle(self, channel):
        value = self.settings[str(channel)]

        print(value)
        
        if value[0] == "1":
            GPIO.output(self.pinRed, not GPIO.input(self.pinRed))

        if value[1] == "1":
            GPIO.output(self.pinGreen, not GPIO.input(self.pinGreen))

        if value[2] == "1":
            GPIO.output(self.pinBlue, not GPIO.input(self.pinBlue))

    def initSettings(self):
        default_settings = '{"5":"001", "6":"010", "13":"100"}'
        
        try:
            f = open("settings.txt","rt")
            print("File settings.txt exists!")
            self.settings = json.loads(f.read())
            print("Settings are", self.settings)
            f.close()

        except FileNotFoundError:
            print("File settings.txt not exists, now we create it and save default settings!")
            f = open("settings.txt","wt")
            f.write(default_settings)
            f.close()
            print("File settings.txt made!")
            print("Settings are",default_settings)
            self.settings = json.loads(f.read())


    def setRoot(self):
        self.root = Tk()
        self.root.geometry("600x100")  # not *
        self.root.title("LOAD AND SAVE SETTINGS")

        # button read and load settings
        btn_save_settings = Button(self.root, text = "SAVE", command = self.saveSettings)
        btn_save_settings.place(x=450,y=50)

        btn_load_settings = Button(self.root, text = "LOAD", command = self.loadSettings)
        btn_load_settings.place(x=500,y=50)

        # labels text fields for settings S1,S2,S3
        lbl_set_s1=Label(self.root, text = "Setting S1")
        lbl_set_s1.place(x=10 , y = 10)

        lbl_set_s2=Label(self.root, text = "Setting S2")
        lbl_set_s2.place(x=160 , y = 10)

        lbl_set_s3=Label(self.root, text = "Setting S3")
        lbl_set_s3.place(x=310 , y = 10)

        # entry text fields for settings S1,S2,S3
        self.string_var_setting_1 = StringVar()  # string_var_setting_1.set("hello") en # string_var_setting_1.get() ipv #entry_set_s1.insert(0,"001")
        self.string_var_setting_2 = StringVar()  
        self.string_var_setting_3 = StringVar()

        entry_set_s1 = Entry(self.root , width= 20 , textvariable= self.string_var_setting_1)
        entry_set_s1.place(x=10 , y=50)
        #string_var_setting_1.set("001") 

        entry_set_s2 = Entry(self.root, width= 20 , textvariable= self.string_var_setting_2)
        entry_set_s2.place(x=160 , y=50)
        #string_var_setting_2.set("010")

        entry_set_s3 = Entry(self.root, width= 20 , textvariable= self.string_var_setting_3)
        entry_set_s3.place(x=310 , y=50)
        #string_var_setting_3.set("100")

    def saveSettings(self):
        self.settings[self.pinBtn1] = self.string_var_setting_1.get()
        self.settings[self.pinBtn2] = self.string_var_setting_2.get()
        self.settings[self.pinBtn3] = self.string_var_setting_3.get()
        
        current_settings = json.dumps(self.settings)
        print(type(current_settings))
        print("Saving current settings as>",current_settings)
        
        try:
            f = open("settings.txt","wt")
            f.write(current_settings)
            f.close
            print("Saved current settings as>",current_settings)
        except FileNotFoundError:
            print("Error during saving")


    def loadSettings(self):
        # loads json from txt file and shows 3 values in the entry fields
        try:
            f = open("settings.txt","rt")
            self.settings = json.loads(f.read())
            f.close()
            print("Settings are",self.settings)
            
            self.string_var_setting_1.set(self.settings["5"])
            self.string_var_setting_2.set(self.settings["6"])
            self.string_var_setting_3.set(self.settings["13"])
                                    
        except FileNotFoundError:    
            print("Error loading settings!")    


    def runLoop(self):
        while True:
            self.root.update()
            


if __name__ == "__main__":
    Domotica()

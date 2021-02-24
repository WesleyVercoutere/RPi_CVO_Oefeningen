import glob  # In Python, the glob module is used to retrieve files/pathnames matching a specified pattern
import os  # os.system om systeem commando's te geven


class TemperatureSensor:

    def __init__(self):
        self.setTemperatureSensor()


    def setTemperatureSensor(self):
        os.system('modprobe w1-gpio')  # enable the one-wire interface 
        os.system('modprobe w1-therm')  # os.system om systeem commando's te geven vanuit python
        
        base_dir = '/sys/bus/w1/devices/w1_bus_master1/'
        device_folder = glob.glob(base_dir + '28*')[0] # In Python, the glob module is used to retrieve files/pathnames matching a specified pattern
        self.device_file = device_folder + '/w1_slave'

    def readTempRaw(self):
        f = open(self.device_file, 'r') #Before you can read or write a file, you have to open it using Python's built-in open() function. This function creates a file object, which would be utilized to call other support methods associated with it.access_mode − The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc. A complete list of possible values is given below in the table. This is optional parameter and the default file access mode is read (r).
        lines = f.readlines()  # Leest alle lijnen in de file. https://www.tutorialspoint.com/python/file_readlines.htm
        f.close()
        #print("lines=",lines)
        return lines
    
    def readTemp(self):
        lines = self.readTempRaw()
        #print("lines2=",lines)    
        if lines[0].strip()[-3:] == 'YES':   #https://www.tutorialspoint.com/python3/string_strip.htm  neemt spaties weg aan begin en einde vd string
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                temp_c = round(temp_c*2)/2
                return temp_c
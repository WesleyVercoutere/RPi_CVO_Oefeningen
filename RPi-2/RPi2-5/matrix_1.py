import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


pin_rij_1 = 18
pin_rij_2 = 23
pin_rij_3 = 24
pin_rij_4 = 25

rijen = (pin_rij_1, pin_rij_2, pin_rij_3, pin_rij_4)

pin_kolom_1 = 12
pin_kolom_2 = 16
pin_kolom_3 = 20
pin_kolom_4 = 21

kolommen = (pin_kolom_1, pin_kolom_2, pin_kolom_3, pin_kolom_4)

GPIO.setup(rijen, GPIO.OUT)
GPIO.setup(kolommen, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

schakelaars = (("S1", 0, 0), ("S2", 1, 0), ("S3", 2, 0), ("S4", 3, 0),
("S5", 0, 1), ("S6", 1, 1), ("S7", 2, 1), ("S8", 3, 1),
("S9", 0, 2), ("S10", 1, 2), ("S11", 2, 2), ("S12", 3, 2),
("S13", 0, 3), ("S14", 1, 3), ("S15", 2, 3), ("S16", 3, 3))

def getButton(rij, kolom):
    
    for schakelaar in range(len(schakelaars)):
        
        if schakelaars[schakelaar][1] == rij and schakelaars[schakelaar][2] == kolom:
            print(f"Schakelaar {schakelaars[schakelaar][0]} ingedrukt.")




def setAllRowsLow():
    GPIO.output(rijen, GPIO.LOW)

def setRowHigh(rij):
    GPIO.output(rijen[rij], GPIO.HIGH)

def readInputs(rij):
    for kolom in range(len(kolommen)):
        if GPIO.input(kolommen[kolom]):
            getButton(rij, kolom)

while True:

    for rij in range(len(rijen)):
        setAllRowsLow()
        setRowHigh(rij)
        readInputs(rij)
        time.sleep(0.01)    

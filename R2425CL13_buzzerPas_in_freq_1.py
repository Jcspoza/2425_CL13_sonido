# Hardware platform: Pico W & Pico _
# Author : JC Santamaria 
# Date : 2023 - 29 -5 
# Goal : External speaker + NPN in GPIO15 - PWM frequency input
# Ref : https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_ac_buz.html

import machine
import utime

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "NPN + Speaker on GPIO15"
p_project = "External speaker with NPN - PWM freq input"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

buzzer = machine.PWM(machine.Pin(15))

def tone(pin,frequency,duration):
    pin.freq(frequency)
    pin.duty_u16(32000) # 50% duty 
    utime.sleep_ms(duration)
    pin.duty_u16(0)

durIn = 250
freqIn =440
while (True): # salir con CTRL+C
    durIn = int(input("Duracion ms (sugerencia 50 a 2000)= "))
    freqIn = int(input("Frecuencia de la onda (sugerencia 20 a 2000)= "))
    tone(buzzer,freqIn,durIn)


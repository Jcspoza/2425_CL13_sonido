# Hardware platform: Pico W & Pico _
# Author : JC Santamaria 
# Date : 2023 - 29 -5 
# Goal : buzzer activo + in GPIO26 - PWM frequency input
# Ref : https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_ac_buz.html

import machine
import utime

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "Active Buzzer in GPIO26"
p_project = "Active Buzzer beep"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

Abuzzer = machine.Pin(26, machine.Pin.OUT)

while True:
    for i in range(4):
        Abuzzer.value(0)
        utime.sleep(0.3)
        Abuzzer.value(1)
        utime.sleep(0.3)
    utime.sleep(1)
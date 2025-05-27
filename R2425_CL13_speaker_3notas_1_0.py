# Hardware platform: Pico W & Pico _
# Author : JC Santamaria 
# Date : 2023 - 29 -5 
# Goal : External speaker + NPN in GPIO15 - simple test sound 3notes
# Ref : https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_ac_buz.html

import machine
import utime

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "NPN + Speaker on GPIO15"
p_project = "External speaker with NPN - simple test sound 3notes"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

buzzer = machine.PWM(machine.Pin(15))

def tone(pin,frequency,duration):
    """Hace sonar un altavoz en 'pin'(+NPN) con onda PWM de frecuencia='frequency' durante 'duration' miliseg     
    """
    pin.freq(frequency)
    pin.duty_u16(40000)
    utime.sleep_ms(duration)
    pin.duty_u16(0)

tone(buzzer,440,250) # LA4
utime.sleep_ms(500)
tone(buzzer,494,250) # SI4
utime.sleep_ms(500)
tone(buzzer,523,250) #DO5

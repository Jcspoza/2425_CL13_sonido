# Hardware platform: Pico W & Pico _
# Author : JC Santamaria 
# Date : 2023 - 29 -5 
# Goal : Play the song Frere J with nested list and tuplas+ External speaker + NPN in GPIO15
# Ref : https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_ac_buz.html
# Get_piano_notes copied from 
# https://github.com/katieshiqihe/music_in_python/blob/main/utils.py
# Author : Katie He katieshiqihe
# and adapteed by my to micropython in Pico


import machine
import utime

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "NPN + Speaker on GPIO15"
p_project = "Play the song Frere J w. list & tuplas- External speaker with NPN - Piano notes"
p_version = "3.1"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# START Functions
def tone(pin,frequency,duration):
    pin.freq(frequency)
    pin.duty_u16(30000)
    utime.sleep_ms(duration)
    pin.duty_u16(0)
    
def silence(pin, duration):
    pin.duty_u16(0)
    utime.sleep_ms(duration)

def get_piano_notes():   
    # Teclas blancas en mayusculas, teclas negra sostenidos en minusculas
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 440 #Frequencia base de La4 o Nota A4
    # Genera una lista de cadenas de caracteres
    # que empiezan por la letras de 'octava'
    # añadiendo un numero de 0 a 9
    # lo hace con dos bucles for anidados dentro de la eexpresion de lista
    ks = [x+str(y) for y in range(0,9) for x in octave]
    # Recorta al teclado standard de A0 a C8
    keys = ks[ks.index('A0'):ks.index('C8')+1]
    # Genera un diccionario con las claves del nombre de letra y los valores de la frecuencia (float)
    # zip empaqueta listas en tuplas
    # dict genera un diccionario con tuplas de 2
    note_freqs = dict(zip(keys, [2**((n+1-49)/12)*base_freq for n in range(len(keys))]))
    return note_freqs # Return a dictionary

# END Functions

buzzer = machine.PWM(machine.Pin(15))

# Old version
# notesFreq = {'C4':262, 'C#4':277, 'D4':294, 'D#4':311, 'E4':330, 'F4':349, 'F#4':370, 'G4':392, 'G#4':415,
#             'A4':440, 'A#4':466, 'B4':494}

notesFreq = get_piano_notes()

# For debug
# for note in sorted(notesFreq.values()):
#     print(note)
#     tone(buzzer,round(note),500)

# print('Notas posibles: las 88 del piano con la siguiente notacion')
# print(notesFreq.keys())

BPM = 150 # Beats per minute para Frere JaqueS
BPMEAS = 4 # 4 /4 Ritmo de Frere Jacques

N = 4 * 60000 // (BPM * BPMEAS) # 60000 = milisegundos en 1 minuto
B = N * 2
C = N // 2
silCompas = N // 32 # arbitrario

# cancion Frere Jacques 8 compases
compasesNotaDur = [[('C4',N), ('D4',N), ('E4',N), ('C4',N)], # COMPAS 1
                  [('C4',N), ('D4',N), ('E4',N), ('C4',N)], # COMPAS 2
                  [('E4',N), ('F4',N), ('G4',B)], # COMPAS 3
                  [('E4',N), ('F4',N), ('G4',B)], # COMPAS 4
                  [('G4',C), ('A4',C), ('G4',C), ('F4',C), ('E4',N), ('C4',N)], # COMPAS 5
                  [('G4',C), ('A4',C), ('G4',C), ('F4',C), ('E4',N), ('C4',N)], # COMPAS 6
                  [('C4',N), ('G4',N), ('C4',B)], # COMPAS 7
                  [('C4',N), ('G4',N), ('C4',B)], # COMPAS 8
                 ]

for comp in range(0, len(compasesNotaDur)):
    for nota in range(0, len(compasesNotaDur[comp])):
        tone(buzzer, round(notesFreq[compasesNotaDur[comp][nota][0]]), compasesNotaDur[comp][nota][1])
        
    silence(buzzer, silCompas)

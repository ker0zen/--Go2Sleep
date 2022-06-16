#A tool by ker0zen


from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import os
import math
import PySimpleGUI as sg
from time import sleep


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))



####GUI####
sg.theme('DarkPurple7')   


layout = [  [sg.Text('Go2Sleep')],
            [sg.Text('Dans combien de temps éteindre l\'ordinateur:'), sg.InputText()],
            [sg.Button('Shut'),sg.Button('Cancel')]]
window = sg.Window('Go2Sleep', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    if event == 'Shut':
        time = int (values [0])
        window.close ()
        currentVolumeDb = volume.GetMasterVolumeLevel ()
        time = float (time * 60)
        sleep(time)
        try:
            while currentVolumeDb > -65.25:
                currentVolumeDb = volume.GetMasterVolumeLevel ()
                volume.SetMasterVolumeLevel (currentVolumeDb - 0.05, None)  #
                sleep (0.2)
        except Exception:
            pass
        os.system ("shutdown /s /t 1")

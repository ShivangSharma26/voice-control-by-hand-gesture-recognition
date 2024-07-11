from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

class VolumeControl:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = interface.QueryInterface(IAudioEndpointVolume)
        volrange = self.volume.GetVolumeRange()
        self.minvol = volrange[0]
        self.maxvol = volrange[1]

    def update_volume(self, length):
        vol = np.interp(length, [0, 168], [self.minvol, self.maxvol])
        volbar = np.interp(length, [0, 168], [400, 150])
        volper = np.interp(length, [0, 200], [-10, 100])
        self.volume.SetMasterVolumeLevel(vol, None)
        return vol, volbar, volper

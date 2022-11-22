import serial
import threading
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import struct
 
class SerialAudioDriver:
  def __init__(self):
    self.devices = AudioUtilities.GetSpeakers()
    self.interface = self.devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))
    self.currentVolume = self.volume.GetMasterVolumeLevelScalar()
    self.communication = serial.Serial('COM3', 9600)
    self.tRead = threading.Thread(target=self.read)
    self.ascii_number = []
    self.string_number = ''
    self.number = 0
    self.run = True
    self.db_range = abs(self.volume.GetVolumeRange()[0])
    self.db_min = abs(self.volume.GetVolumeRange()[0])
 
  def change_volume(self, nuevo_volumen):
    self.currentVolume = nuevo_volumen / 100
    self.volume.SetMasterVolumeLevelScalar(self.currentVolume, None)
 
  def release(self):
    for ascii in self.ascii_number:
      self.string_number+= ascii
    nuevo_volumen = int(self.string_number)
    self.ascii_number = []
    self.string_number= ''
    self.change_volume(nuevo_volumen)
    self.write()
 
  def read(self):
    while self.run:
      value = self.communication.read(1)
      if value != None:
        if value.decode("utf-8") == "\n" or value.decode("utf-8") == "\r":
          pass
        elif value.decode("utf-8") == "#":
          pass
        elif value.decode("utf-8") == "*":
          self.release()
        else:
          self.ascii_number.append(value.decode("utf-8"))
 
  def write(self):
    self.communication.write(str(self.currentVolume*100).encode('utf-8'))
      
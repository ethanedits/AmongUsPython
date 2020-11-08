import pymem
import time
import keyboard
from pymem.process import module_from_name

mem = pymem.Pymem("Among Us.exe")

def dmaAddr(base, offsets):
  addr = mem.read_int(base)
  for i in offsets:
    addr = mem.read_int(addr + i)
  return addr

speedVal = 10.0
imposterVal = 1
ghostVal = 1

while True:

    #Speed Cheat
    if keyboard.is_pressed("F1"):
        mem.write_float(dmaAddr(module_from_name(mem.process_handle, "GameAssembly.dll").lpBaseOfDll + 0x0144BB70, [0x5C, 0x4]) + 0x14, speedVal)

        if speedVal == 10.0:
            speedVal = 1.0
            time.sleep(1)
        else:
            speedVal = 10.0
            time.sleep(1)

    #Force Imposter Cheat
    if keyboard.is_pressed("F2"):
        mem.write_int(dmaAddr(module_from_name(mem.process_handle, "GameAssembly.dll").lpBaseOfDll + 0x0144BB70, [0x5C, 0x0, 0x34]) + 0x28, imposterVal)

        if imposterVal == 1:
            imposterVal = 0
            time.sleep(1)
        else:
            imposterVal = 1
            time.sleep(1)

    #Ghost Cheat
    if keyboard.is_pressed("F3"):
        mem.write_int(dmaAddr(module_from_name(mem.process_handle, "GameAssembly.dll").lpBaseOfDll + 0x0144BB70, [0x5C, 0x0, 0x34]) + 0x29, ghostVal)

        if ghostVal == 1:
            ghostVal = 0
            time.sleep(1)
        else:
            ghostVal = 1
            time.sleep(1)

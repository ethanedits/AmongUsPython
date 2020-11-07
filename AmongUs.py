import pymem, time, keyboard, os, colorama, random
colorama.init()

def dmaAddr(base, offsets):
  addr = mem.read_int(base)
  for i in offsets:
    addr = mem.read_int(addr + i)
  return addr

def Module(handle, name, plus, offsets):
    first = pymem.process.module_from_name(handle.process_handle, name).lpBaseOfDll + plus
    last = dmaAddr(first,offsets)
    return last

mem = pymem.Pymem("Among Us.exe")

speedVal = 10.0
EnableImposter = False
EnableGhost = False


colors = list(vars(colorama.Fore).values())

os.system("cls")
print(random.choice(colors) + "AmongUs Cheat | EthanEdits")
print("----------------------------------------------------------")
print("F1 = Speed")
print("F2 = ForceImposter")
print("F3 = Ghost")
print("---------------------------")    
print("Console:")

while True:
    randomcolor = random.choice(colors)

    Speed = Module(mem,"GameAssembly.dll",0x0144BB70,[0x5C, 0x4])
    FImposter = Module(mem,"GameAssembly.dll",0x0144BB70,[0x5C, 0x0, 0x34])
    Ghost = Module(mem,"GameAssembly.dll",0x0144BB70,[0x5C, 0x0, 0x34])

    if keyboard.is_pressed("F1"):
        time.sleep(0.2)

        if speedVal == 10.0:
            speedVal = 1.0
        else:
            speedVal = 10.0
        mem.write_float(Speed + 0x14, speedVal)

    if keyboard.is_pressed("F2"):
        time.sleep(0.2)
        EnableImposter = not EnableImposter

        mem.write_int(FImposter + 0x28, int(EnableImposter))

        if EnableImposter:
            print(randomcolor + "ForceImposter Activated")
        else:
            print(randomcolor + "ForceImposter Deactivated")
    
    if keyboard.is_pressed("F3"):
        time.sleep(0.2)
        EnableGhost = not EnableGhost

        mem.write_int(Ghost + 0x29, int(EnableGhost))

        if EnableGhost:
            print(randomcolor + "Ghost Activated")
        else:
            print(randomcolor + "Ghost Deactivated")

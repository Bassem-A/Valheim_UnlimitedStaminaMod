import pymem
import pymem.process
import pymem.memory




process = pymem.process
mem = pymem.memory

#address1 = 0x24BDB4B7B9C
address2 = "UnityPlayer.dll+18053F0"
pm = pymem.Pymem("valheim.exe")
game_base = pm.process_handle
offsets = [0x8,0x0,0x8,0x10,0x28,0x8,0x10,0x28,0x18,0x558]
value = 75.00
client = pymem.process.module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll
#UnityPlayer.dll+18053F0
base = pm.read_longlong(client+0x18053F0)
for i in range(9):
	base = offsets[i]+base
	base = pm.read_longlong(base)
	
	
base=base+0x558


print("unlimited Stamina ON...")

while(1):
	pm.write_float( int(base), value)
	
	
	
	
	



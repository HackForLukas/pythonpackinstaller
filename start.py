import os
name = "pip"
version = int(input("Your python version 1-2-3: "))
if version == 1:
	pass
else:
	name += str(version)
print("\nPython Package İnstaller")
while True:
	names = input("\nPython Packet Name > ")
	os.system(f"{name} install {names}")

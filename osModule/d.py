import os
os.chdir("/Users/karth/Desktop/SEM5")

for dirpath,dirnames,filenames in os.walk("/Users/karth/Desktop/SEM5"):
	print("Current path",dirpath)
	print("directories",dirnames)
	print("files",filenames)
	print()

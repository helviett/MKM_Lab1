import os
import re
import platform

files = os.listdir('ui') 
print('----------------Start----------------')

fincludes = open('includes.txt', 'w')
for file in files:
	newfile = file.replace(".ui", ' ')
	fincludes.write(newfile + '\n')

print('----includes.txt was created')
fincludes.close()

for file in files:
	print('----' + file + ':')
	newfile = file.replace(".ui", ' ')
	if platform.system() == 'Windows':
		bashCommand = 'python compiler.py ' + newfile
	else:
		bashCommand = 'python3 compiler.py ' + newfile
	os.system(bashCommand)

print('---------------Finish----------------')
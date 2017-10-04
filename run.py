import os
import re

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
	bashCommand = 'python compiler.py ' + newfile
	os.system(bashCommand)

print('---------------Finish----------------')
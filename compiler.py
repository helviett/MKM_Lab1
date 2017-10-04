import sys
import os

obj = sys.argv[1]

bashCommand = 'pyuic5 ui/' + obj + '.ui -o Windows/' + obj + '.py'
os.system(bashCommand)
print('--------Windows/'+ obj + '.py was created')

fcode = open('FormsCode/' + obj + '.py')
fin = open('Windows/' + obj + '.py')
fout = open('GenCode/' + obj + '.py', 'w')
fincludes = open('includes.txt')


fout.write('from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow\n')
for module in (line.rstrip() for line in fincludes.readlines()):
	if (module != obj):
		fout.write('from GenCode.' + module + ' import ' + '*\n')

flag = False
for line in fin:
	if (line.find('def setupUi') > 0): flag = True
	elif (flag and line.find('def ') > 0):
		fout.write('        self.initialize(MainWindow)\n\n')
		flag = False
	
	fout.write(line)


for line in fcode:
	fout.write('    ' + line)
print('--------GenCode/'+ obj + '.py was created')
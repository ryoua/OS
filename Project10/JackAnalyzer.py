import JackTokenizer
import CompilationEngine
import sys,os
 
filename=sys.argv[1]
readfile = open(filename,'r')
 
copyfile = open('copyfile','w')
line=readfile.readline()
while line:
	while line == '\n' or line.startswith('//'):
		line=readfile.readline()
	if '//' in line:
		line=line[:line.find('//')]
	if '/*' in line:
		aline=line[:line.find('/*')]
		while line.find('*/')<0:
			line=readfile.readline()
		bline=line[line.find('*/')+2:]
		line=aline+bline
	copyfile.write(line)
	line=readfile.readline()
copyfile.close()
readfile.close()
 
rfile=open('copyfile','r')
wfile=open(filename.strip('.jack')+'.xml','w')
 
CompilationEngine.compileClass(rfile,wfile)
 
rfile.close()
wfile.close()
os.remove('copyfile')
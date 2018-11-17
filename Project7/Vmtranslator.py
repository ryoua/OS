import sys, os
from Project7 import CodeWriter, Parser

filename = sys.argv[1]
rfile = open(filename, 'r')
wfile = CodeWriter.setFileName(filename)
wfile.write('@256\nD=A\n@SP\nM=D\n')
line = Parser.advance(rfile)
flag = Parser.hasMoreCommands(line)
while flag:
    while line == '\n' or line.startswith('//'):
        line = rfile.readline()
    ctype = Parser.commandType(line)
    if ctype == 'C_ARITHMATIC':
        attribute1 = Parser.arg1(line).strip()
        CodeWriter.writeArithmatic(wfile, attribute1)
    elif ctype in ('C_PUSH', 'C_POP'):
        attribute1 = Parser.arg1(line).strip()
        attribute2 = Parser.arg2(line).strip()
        CodeWriter.writePushPop(wfile, ctype, attribute1, attribute2, filename)
    line = Parser.advance(rfile)
    flag = Parser.hasMoreCommands(line)

rfile.close()

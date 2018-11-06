import sys
import Parser
import SymbolTable

filename = sys.argv[1]
ifile = open(filename, 'r')
strfile = ifile.read()
instr = strfile.split('\n')
i=0
l1 = ['', '\r', '\n']
instr_str = []
for x in instr:
    if not x.startwith('//'):
        if x not in l1:
            instr_str.append(x.strip('\r'))

address = 16
sym = SymbolTable.Constructor()

for x in instr_str:
    if x.find('@') >= 0 or x.find('(') >= 0:
        symbol = Parser.symbol(x)
        if not SymbolTable.contains(symbol, sym) and not symbol.isdigit():
            sym = SymbolTable.addEntry(symbol, address, sym)
            address = address + 1

while Parser.hasMoreCommands(i, instr_str):
    c_type = Parser.commandType(instr_str[i]) 
    if c_type == 'A':
        str1 = Parser.symbol(instr_str[i])
        if str1.isdigit():
            str1 = bin(int(str1))[2:]
            address = str1.zfill(16)
            print(address)       
        else:
            if SymbolTable.contains(str1, sym):
                str2 = bin(SymbolTable.GetAddress(str1, sym))[2:] 
                address1 = str2.zfill(16)
                print(address1)
    if c_type == 'C':
        c_str = Parser.comp(instr_str[i])
        d_str = Parser.dest(instr_str[i])
        j_str = Parser.jump(instr_str[i])
        print('111' + c_str + d_str + j_str)
    i = i + 1
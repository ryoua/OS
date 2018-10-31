import re

from Code import dest, comp, jump


def commandType(line):
    pattern_A = re.compile(r'@\w+')
    pattern_C = re.compile(r'\w+=\w+|\w+=\w+;')
    pattern_L = re.compile(r'\([a-z]+\)|\([A-Z]+\)')
    match_A = pattern_A.match(line)
    match_C = pattern_C.match(line)
    match_L = pattern_L.match(line)
    if match_A:
        return "A_COMMAND"
    elif match_C:
        return "C_COMMAND"
    elif match_L:
        return "L_COMMAND"


def main():
    f = open('Mult.hack', 'w+')
    f.write('')
    f = open('Mult.asm', 'r')
    for line in f.readlines():
        line = line.strip()
        if not len(line):
            continue
        if (commandType(line) == "A_COMMAND") | (commandType(line) == "L_COMMAND"):
            pass
        elif commandType(line) == 'C_COMMAND':
            if line.split('='):
                line_dest = line.split('=')[0]
                line_comp = line.split('=')[1]
                # line_jump = line.split('=')[1].split(';')[1]
                line_jump = "Null"

            else:
                line_dest = "Null"
                line_comp = line.split(';')[0]
                line_jump = line.split(';')[1]

            Binary_dest = dest(line_dest)
            print(Binary_dest)
            Binary_comp = comp(line_comp)
            print(Binary_comp)
            Binary_jump = jump(line_jump)
            print(Binary_jump)

            Binary_Code = Binary_dest + Binary_comp + Binary_jump
            print(Binary_Code)
            print('------------------------------')
            with open('Mult.hack', 'a') as f:
                f.write(Binary_Code+'\n')

main()




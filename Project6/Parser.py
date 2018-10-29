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
    f = open('Mult.asm', 'r')
    for line in f.readlines():
        line = line.strip()
        if not len(line):
            continue
        if (commandType(line) == "A_COMMAND") | (commandType(line) == "L_COMMAND"):
            # symbol(line)
            print('123123132131')
            pass
        elif commandType(line) == 'C_COMMAND':
            line_dest = line.split('=')[0]
            line_comp = line.split('=')[1].split(';')[0]
            line_jump = line.split('=')[1].split(';')[1]

            Binary_dest = dest(line_dest)
            Binary_comp = comp(line_comp)
            Binary_jump = jump(line_jump)

            Binary_Code = Binary_dest + Binary_comp + Binary_jump
            print("1111111")
            f = open('Mult.hack', 'w+')
            f.write(Binary_Code)

main()




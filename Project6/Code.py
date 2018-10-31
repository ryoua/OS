def dest(line):
    dests = ['Null', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
    bits = ['000', '001', '010', '011', '100', '101', '110', '111']
    subscript = dests.index(line)
    return bits[subscript]


def comp(line):
    comps_a = ['0', '1', '-1', 'D', 'A', '!D',
               '!A', '-D', '-A', 'D+1', 'A+1', 'D-1',
               'A-1', 'D+A', 'D-A', 'A-D', 'D&A', 'D|A']
    comps = ['0', '1', '-1', 'D', 'M', '!D',
             '!M', '-D', '-M', 'D+1', 'M+1', 'D-1',
             'M-1', 'M+D', 'D-M', 'M-D', 'D&M', 'D|M']
    bits = ['101010', '111111', '111010', '001100', '110000', '001101',
            '110001', '001111', '110011', '011111', '110111', '001110',
            '110010', '000010', '010011', '000111', '000000', '010101']
    if line in comps_a:
        subscript = comps_a.index(line)
        return '0' + bits[subscript]
    elif line in comps:
        subscript = comps.index(line)
        return '1' + bits[subscript]


def jump(line):
    jumps = ['Null', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
    bits = ['000', '001', '010', '011', '100', '101', '110', '111']
    subscript = jumps.index(line)
    return bits[subscript]

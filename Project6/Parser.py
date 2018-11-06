import Code

def hasMoreCommands(i, list):
    if i >= len(list):
        return 0
    else:
        return 1


def advance(i):
    return i + 1


def commandType(line):
    if line.find('@') >= 0:
        return 'A'
    elif line.find('=') >= 0 or line.find(';') >= 0:
        return 'C'
    elif line.find('(') >= 0:
        return 'L'


def symbol(line):
    symbolflag = line.strip(' @()\n\r')
    return symbolflag


def dest(line):
    if line.find('=') > 0:
        destlist1 = line.split('=')
        return Code.dest(destlist1[0].strip(' '))
    elif line.find(';') >= 0:
        return Code.dest('null')


def comp(line):
    if line.find('=') > 0:
        complist1 = line.split('=')
        return Code.comp(complist1[1].strip('\n'))
    elif line.find(';') >= 0:
        complist2 = line.split(';')
        return Code.comp(complist2[0].strip(' '))


def jump(line):
    if line.find('=') >= 0:
        return Code.jump('null')
    elif line.find(';') >= 0:
        jumplist = line.split(';')
        return Code.jump(jumplist[1].strip(' \n'))

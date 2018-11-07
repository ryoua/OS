import sys, os
import Project7.Parser
CODEFLAG1 = 0
CODEFLAG2 = 0


def setFileName(filename):
    filetuple = os.path.splitext(filename)
    wfile = open(filetuple[0] + '.asm', 'w')
    return wfile


def writeArithmetic(wfile, command):



def WritePushPop():
    pass

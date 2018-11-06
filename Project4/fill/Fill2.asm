// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(LOOP)

// 初始化屏幕指针
@SCREEN
D=A
@pointer
M=D

// 当按下键盘时，填充屏幕
@KBD
D=M
@FILL
D;JGT

@LOOP
0;JMP

(END)

// 当松开键盘时，清理屏幕
@KBD
D=M
@CLEAN
D;JEQ

(FILL)
@pointer
A=M
M=-1
@pointer
M=M+1
@pointer
D=M
@KBD
D=D-A
@LOOP
D;JEQ

@KBD
D=M
@CLEAN
D;JEQ

@FILL
0;JMP
(END_FILL)

(CLEAN)
@pointer
A=M
M=0
@pointer
M=M-1
@pointer
D=M
@16383
D=D-A
@LOOP
D;JEQ
@CLEAN
0;JMP
(END_CLEAN)

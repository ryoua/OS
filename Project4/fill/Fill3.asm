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

    @END
    0;JMP

// 填充屏幕
(FILL)
    @pointer
    A=M
    M=-1
    @pointer
    M=M+1

    // 如果填充满整个屏幕，则执行(END)
    @pointer
    D=M
    @KBD
    D=D-A
    @END
    D;JEQ

    // 如果填充过程中松开，则执行(CLEAN)
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
    
    // 如果清理完成，则返回(LOOP)
    @pointer
    D=M
    @16383
    D=D-A
    @LOOP
    D;JEQ
    
    @CLEAN
    0;JMP
(END_CLEAN)

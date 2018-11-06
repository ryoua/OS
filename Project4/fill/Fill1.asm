// define max screen (24576)
@24576
D=A
@MXSCREEN
M=D


// define screen pointer (16384)
@SCREEN
D=A
@POINTER
M=D


(LOOP)     // infinite loop
  // If we have keyboard input, jump to FILL
  @KBD
  D=M
  @FILL
  D; JGT

  // Otherwise jump to UNFILL
  @UNFILL
  0; JMP


(UNFILL)
  // Do nothing if POINTER == SCREEN
  @SCREEN
  D=A
  @POINTER
  D=D-M
  @LOOP
  D; JEQ

  // Unfill the screen
  D=0
  @POINTER
  A=M
  M=D

  // Decrement POINTER
  D=1
  @POINTER
  D=M-D
  @POINTER
  M=D

  // Jump back to main loop
  @LOOP
  0; JMP


(FILL)
  // Do nothing if the screen is full
  @MXSCREEN
  D=M
  @POINTER
  D=D-M
  @LOOP
  D; JEQ


  // Fill in the pixel that POINTER points to
  //@-1
  D=-1
  @POINTER
  A=M
  M=D

  // Iterate pointer by 1
  D=1
  @POINTER
  D=D+M
  @POINTER
  M=D

  // jump back to main loop
  @LOOP
  0; JMP
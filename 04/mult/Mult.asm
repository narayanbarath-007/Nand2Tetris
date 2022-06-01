// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
@1 
D=M // D = RAM[1]
@3
M=D // RAM[3]=D D=RAM[1]
@2
M=0
(LOOP) //Start of the loop
@3
D=M // D = RAM[3] 
@END
D;JEQ // IF D = 0 then end the loop
@0 
D=M // Loads the value of RAM[0]
@2
M=M+D //This adds the value of RAM[0] to RAM[2] 
@3
M=M-1 // This decreases the value of RAM[3] by 1
@LOOP
0;JMP
(END)
@END
0;JMP



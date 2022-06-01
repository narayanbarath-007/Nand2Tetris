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
	@SCREEN
	D=A
	@0
	M=D //This ensures D contains the location of the screen
	//M[0] = Screen
    @KBD
	D=M 
	@WHITE
	D;JEQ // TO check if keyboard value is 0 or not
	@SCREEN
	(BLACK)
	@1
	M=-1
	@Colour
	0;JMP
	(WHITE)
	@1
	M=0
	(KBDCHK)

	@Colour
	0;JMP
	// M[1] contains the colour
	(Colour)
	@1
	D=M // D contains the colour to be filled with 

	@0
	A=M
	M=D // The pixel is coloured

	@0
	M=M+1 
	
	@KBD
	D=A
	
	@0
	D=D-M
	
	@Colour
	D;JGT // This ensures that if the full screen is not coloured it will continue colouring

	@LOOP
	0;JMP



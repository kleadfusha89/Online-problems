TITLE Klead Fusha 

INCLUDE Irvine32.inc

.data
	roll	DWORD ?
	roll2	DWORD ?
	plus	BYTE " + ", 0
	equal	BYTE " = ", 0
	uWin	BYTE "You Win. You total was ", 0
	uLose	BYTE "You Lose. Your total was ", 0
	uTie	BYTE "That's a tie. Your total was ", 0

	testing	BYTE "TESTING: ", 0
.code
main PROC
again:

	call Randomize
    mov  eax,6    
    call RandomRange
	inc	 eax					; Random number from 1 to 6
    mov  roll,eax				; Store the vlaue into the variable roll
	call WriteDec				; Print its value

	mov edx, OFFSET plus		; Print the plus sign 
	call WriteString

	call Randomize
    mov  eax,6    
    call RandomRange			; Second roll, get random number 1 - 6
	inc  eax
    mov  roll2,eax				; Store the value in the variable roll2
	call WriteDec				; Print its value

	mov edx, OFFSET equal		; Print the equal sign
	call WriteString

	mov eax, roll				; Move into eax the value of roll 1
	add eax, roll2				; and add the value of the second roll to it

	call WriteDec				; Print the total we just added
	call Crlf

	;---------------------------------------
	; Comparing it to the respective values
	; and depending on the result jump to
	; a winner or loser label. If no winner
	; or loser this time, start all over
	; again
	;---------------------------------------
	cmp eax, 6
	je	winner
	cmp eax, 8
	je winner
	cmp eax, 9
	je loser
	cmp eax, 5
	je loser

	mov edx, OFFSET uTie			; Print a tie message
	call WriteString
	call WriteDec					; Show the tie result
	call Crlf
	jmp again						; Start rolling all over again

winner:
	mov edx, OFFSET uWin			; Print winner message
	call WriteString
	call WriteDec					; Show result
	call Crlf
	jmp done						; Go to end of program

loser:
	mov edx, OFFSET uLose			; Print loser message
	call WriteString

	Call WriteDec					; Show total result
	call Crlf

done:
	call WaitMsg

	exit
main ENDP
END main
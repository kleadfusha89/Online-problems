TITLE Klead Fusha Final Question 4

INCLUDE Irvine32.inc

.data
	minus	BYTE " - ", 0
	equal	BYTE " = ", 0
	mssg	BYTE "Count: ", 0
	num		DWORD 27
.code

sqrt PROC
	push ebp
	mov ebp, esp
	sub esp, 8				; Creating room for two local variables
	
	mov eax, 1				; Populating the first variable
	mov [ebp - 4], eax      ; int inc = 1
	
	mov eax, 0				; Populating the second local variable
	mov [ebp - 8], eax		; int count = 0

again:
	mov eax, [ebp - 4]		; If the inc variable is greater than the argument we passed
	cmp eax, [ebp + 8]		; skip the loop
	jg done

	mov eax, [ebp - 8]		; count += 1
	inc eax
	mov [ebp - 8], eax

	mov eax, [ebp + 8]		; Print the argument (which will be subtrcted eventually)
	call WriteDec

	mov edx, OFFSET minus	; Print a minus sign
	call WriteString

	mov eax, [ebp - 4]		; Print the inc variable (which will prin the odd numbers)
	call WriteDec

	mov edx, OFFSET equal	; Print an equal sign
	call WriteString


	mov eax, [ebp + 8]		; sqrt = sqrt - inc
	sub eax, [ebp - 4]
	mov [ebp + 8], eax

	mov eax, [ebp - 4]		; inc += 2
	add eax, 2
	mov [ebp - 4], eax

	mov eax, [ebp + 8]		; Print the value of the argument we passed
	call WriteDec

	call Crlf
	jmp again				; Looping
done:
	mov eax, [ebp - 8 ]		; Store to the eax register the value of the total number of subtractions

	add esp, 8
	pop ebp
	ret 4
sqrt ENDP


main PROC
	push num				; The argument we've passed
	call sqrt

	call Crlf

	mov edx, OFFSET mssg	; Write the final message
	call WriteString

	call WriteDec
	call Crlf
	call WaitMsg
	exit
main ENDP
END main
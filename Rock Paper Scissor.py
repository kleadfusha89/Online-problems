import random


def main():

    user = 'a'  

    computer = 1  
    tie = 0  
    win = 0 
    lose = 0 

	while user != 'X':

        print()

   
        user = input('Choose (r)ock, (s)cissor, (p)aper or e(x)it: ')

      
        while user != 'R' and user != 'r' and user != 'P' and user != 'p' and user != 'S'\
                and user != 's' and user != 'x' and user != 'X':

            print() 
            print('ERROR. Please enter a valid choice!')  

         
            user = input('Choose (r)ock, (s)cissor, (p)aper or e(x)it: ')

 
        get_computer_selection(computer)

        get_user_selection(user)

       
        computer = get_computer_selection(computer)

      
        user = get_user_selection(user)

       
        if user == 'R' and computer == 'R':
            print('Computer picked rock. It\'s a tie')
            tie += 1

     
        if user == 'P' and computer == 'R':
            print('Computer picked rock. Paper covers rock. YOU WIN!!!')
            win += 1


        if user == 'S' and computer == 'R':
            print('Computer picked rock. Rock blunts scissor. You lose.')
            lose += 1

     
        if user == 'R' and computer == 'P':
            print('Computer picked paper. Paper covers rock. You lose.')
            lose += 1

       
        if user == 'P' and computer == 'P':
            print('Computer picked paper. It\'s a tie')
            tie += 1

       
        if user == 'S' and computer == 'P':
            print('Computer picked paper. Scissor cuts paper. You WIN!!!')
            win += 1

     
        if user == 'R' and computer == 'S':
            print('Computer picked scissor. Rock blunts scissor. You WIN!!!')
            win += 1

      
        if user == 'P' and computer == 'S':
            print('Computer picked scissor. Scissor cuts paper. You lose.')
            lose += 1

     
        if user == 'S' and computer == 'S':
            print('Computer pickes scissor. It\'s a tie')
            tie += 1



    print('Results:')  

    print('        You won', win, 'time(s)')  
    print('        You lost', lose, 'time(s)')
    print('        There were', tie, 'tie(s)')  



def get_computer_selection(computer_choice):


    computer_choice = random.randint(0, 2)

  

    if computer_choice == 0:
        return 'R'
    if computer_choice == 1:
        return 'P'
    if computer_choice == 2:
        return 'S'


def get_user_selection(user_choice):

    if user_choice == 'x' or user_choice == 'X':
        return 'X'

   
    if user_choice == 'r' or user_choice == 'R':
        return 'R'

   
    if user_choice == 'p' or user_choice == 'P':
        return 'P'


    if user_choice == 's' or user_choice == 'S':
        return 'S'


main()

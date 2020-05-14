
FILE_NAME = 'output.csv'


def main():

    print('\n** Klead Fusha **\n') 

 
    do_another = 'y'

    output_file = open(FILE_NAME, 'w')  

    output_file.write('Soccer team,League,National trophies,International trophies' + '\n')

    print() 
    print('You will be asked to enter information about soccer teams')

    print()  
    while do_another == 'y' or do_another == 'Y':

  
        print('---------------------------------------------------------')

      
        soccer_team = input(format('Enter soccer team name: ', '45s'))

       
        league = input(format('Enter the league where it plays: ', '45s'))

       
        national_trophies = int(input(format('Total number of national trophies won: ', '45s')))

 
        int_trophies = int(input(format('Total number of international trophies won: ', '45s')))

        print()  


        do_another = input(format('Do you want to add another Team (y/n)?: ', '45s'))

        print() 

   
        while do_another != 'y' and do_another != 'n' and do_another != 'Y' and do_another != 'N':

            
            do_another = input(format('          Error! Please enter \'y\' or \'n: ', '35s'))

            print() 

     
        output_file.write(soccer_team + ',')

   
        output_file.write(league + ',')

      
        output_file.write(str(national_trophies) + ',')

 
        output_file.write(str(int_trophies) + '\n')

    
    output_file.close()


main()

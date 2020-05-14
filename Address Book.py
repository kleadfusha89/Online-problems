
def main():
  

   
    SIZE = 3

    names = [0.0] * SIZE 
    phones = [0.0] * SIZE  
    emails = [0.0] * SIZE  
    
    for counter in range(0, SIZE):

    
        print(format('Enter name #' + str(counter + 1) + str(':'), '25s'), end='')
        names[counter] = input()

     
        print(format('Enter phone numer #' + str(counter + 1) + str(':'), '25s'), end='')
        phones[counter] = input()

      
        print(format('Enter email address #' + str(counter + 1) + str(':'), '25s'), end='')
        emails[counter] = input()

        print()  

    print()
    search_value = input('Enter search value: ')  

    
    counter = 0


    while counter == 0 and names[counter].find(search_value) != -1 and search_value != '':

     
        print('Name                    Phone              Email')
        print('----                    -----              -----')

  
        print(format(names[counter], '24s'), end='')  
        print(format(phones[counter], '19s'), end='')  
        print(emails[counter])

       
        counter += 1

       
        while counter < len(names) and names[counter].find(search_value) != -1:

            print(format(names[counter], '24s'), end='')  
            print(format(phones[counter], '19s'), end='')  
            print(emails[counter])  

            counter += 1 

            
            if names[counter].find(search_value) == -1:
                counter += 1

        
        while counter < len(names) and names[counter].find(search_value) == -1:

            counter += 1 

            
            while counter < len(names) and names[counter].find(search_value) != -1:

                print(format(names[counter], '24s'), end='')  
                print(format(phones[counter], '19s'), end='') 
                print(emails[counter]) 

                counter += 1  

        print()  

        
        search_value = input('Enter search value: ')
        
        counter = 0

  
    while counter < len(names) and names[counter].find(search_value) == -1 and search_value != '':

       
        print('Name                    Phone              Email')
        print('----                    -----              -----')

       
        while counter < len(names) and names[counter].find(search_value) == -1:

            counter += 1 

           
            while counter < len(names) and names[counter].find(search_value) != -1:

                print(format(names[counter], '24s'), end='') 
                print(format(phones[counter], '19s'), end='')  
                print(emails[counter]) 

                counter += 1  

        print() 

       
        search_value = input('Enter search value: ')
        counter = 0 


main()

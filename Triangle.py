def main():

    print('\n** Klead Fusha **\n') 
    menu_string = 1 


    while menu_string != '4':

        print('1. Calculate the area of a circle.')
        print('2. Calculate the area of a rectangle.')
        print('3. Calculate the area of a triangle.')
        print('4. Quit program.')

        print() 

        valid = False 

        menu = 0.0 

     
        menu_string = input('Enter your choice: ')

        print()  # Blank line

        
        while not valid:

            if is_float(menu_string):
                menu = float(menu_string)  

             
                if menu >= 1 and menu <= 4:
                    valid = True

            if not valid:

                print()  
                print('Please enter a valid option from the menu!') 

                print() 

              
                print('1. Calculate the area of a circle.')
                print('2. Calculate the area of a rectangle.')
                print('3. Calculate the area of a triangle.')
                print('4. Quit program.')

                print()  

                menu_string = input('Please re-enter a valid choice: ')
                print()  

      
        if menu == 1:
            circle_area()

      
        elif menu == 2:
            rectangle_area()

       
        elif menu == 3:
            triangle_area()


def circle_area():

    print('----Area of a circle----')  

 
    radius_string = input('Please enter the radius of the circle: ')

    valid = False  
    radius = 0.0 

    
    while not valid:

        if is_float(radius_string):
            radius = float(radius_string)  

          
            if radius > 0:
                valid = True

      
        if not valid:
            print() 

         
            print('Error!!! Please enter a value greater than 0')

            radius_string = input('Radius of the circle: ')
            print()

    
    area = 3.14159 * radius * radius

    print()

  
    print('The area of the the circle is equal to ', end='')
    print(round(area, 2))

    print()  

    print('--------------------------------------')  


def rectangle_area():

    print('----Area of a rectantle----')
    print() 

   
    length_string = input('Please enter the length of the rectangle: ')

    length = 0.0 

    valid = False  

    
    while not valid:

        if is_float(length_string):
            length = float(length_string)  

        
            if length > 0:
                valid = True

     
        if not valid:
            print()  

          
            print('Error! The length of the rectangle should be va value greater than 0.')
            length_string = input('Please enter the length of the rectangle: ')

    width_string = input('Please enter the width of the rectangle: ')

    width = 0.0  
    valid = False  

   
    while not valid:

        if is_float(width_string):
            width = float(width_string)  

     
            if width > 0:
                valid = True

     
        if not valid:

            print() 

       
            print('Error! The width of the rectangle should be a value greater than 0.')

            width_string = input('Please enter the width of the rectangle: ')

    area = length * width  

    print()  

   
    print('The area of the rectangle is equal to ', end='')
    print(round(area, 2))

    print()  
    print('--------------------------------------') 


def triangle_area():

    print('----Area of a triangle----')  
    print()  

   
    base_string = input('Please enter the length of the triangles\'s base: ')

    base = 0.0 

    valid = False  
  
    while not valid:

        if is_float(base_string):
            base = float(base_string)  

         
            if base > 0:
                valid = True

      
        if not valid:

            base_string = input('ERROR! Please enter a value greater than 0: ')

  
    height_string = input('Please enter the length of the triangle\'s height: ')
    height = 0.0 

    valid = False 

  
    while not valid:

        if is_float(height_string):
            height = float(height_string)  


            if height > 0:
                valid = True

    
        if not valid:

           
            height_string = input('ERROR! Please enter a value greater than 0: ')


    area = base * height * 0.5

    print() 


    print('The area of the triangle is equal to ', end='')
    print(round(area, 2))

    print()
    print('--------------------------------------')  



def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return


main()

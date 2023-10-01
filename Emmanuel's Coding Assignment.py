#Defining each operation
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    #Handle the zero error
    if y == 0:
        return "Error: Cannot divide by zero" 
    else:
        return x / y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number"
    else:
        return x ** 0.5
        
        
#Define the calculator
def calculator():
    while True: #Loop the calculator operation
        print("Welcome to the Ultimate Calculator")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Quit")
    
        #Choose an operation
        selection = input("Enter choice (1/2/3/4/5/6): ")
    
        #Make sure the choice is valid
        if selection not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please pick from the options provided.")
            print()
            print()
            
        else:
            if selection == '6':
                print("Terminating Calculator. Goodbye.")
                break   #Terminate program if user quits
            else:
                #Request the first number
                num1 = float(input("Enter first number: "))
                if selection != '5':  #Since square root only needs on number
                    num2 = float(input("Enter second number: "))
                
                #Use operation requested to provide result
                if selection == '1':
                    result = addition(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                    print()
                    print()
                    
                    
                elif selection == '2':
                    result = subtraction(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                    print()
                    print()
                    
                elif selection == '3':
                    result = multiplication(num1, num2)
                    print(f"Result: {num1} * {num2} = {result}")
                    print()
                    print()
                    
                elif selection == '4':
                    result = division(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
                    print()
                    print()
                    
                elif selection == '5':
                    result = square_root(num1)
                    print(f"The square root of {num1} is {result} ")
                    print()
                    print()
                
calculator()

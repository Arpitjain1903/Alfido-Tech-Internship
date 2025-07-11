def calculator():
    print("Basic Arithmetic Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            # User selects operation
            choice = input("Enter operation number (1/2/3/4) or 'q' to quit: ")
            
            if choice.lower() == 'q':
                print("Exiting calculator. Goodbye!")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please try again.")
                continue
            
            # Input two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
        
        except ValueError:
            print("Invalid input! Please enter numbers only.")

# Run the calculator
calculator()
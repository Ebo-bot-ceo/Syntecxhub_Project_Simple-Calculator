# =========== TASK 1: SIMPLE CALCULATOR ===========

def add(a, b):
    """Addition function"""
    return a + b

def subtract(a, b):
    """Subtraction function"""
    return a - b

def multiply(a, b):
    """Multiplication function"""
    return a * b

def divide(a, b):
    """Division function with zero check"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_valid_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def perform_calculation(operation, num1, num2):
    """Perform calculation based on operation choice"""
    operations = {
        1: ("+", add),
        2: ("-", subtract),
        3: ("*", multiply),
        4: ("/", divide)
    }
    
    if operation not in operations:
        raise ValueError("Invalid operation")
    
    symbol, func = operations[operation]
    
    try:
        result = func(num1, num2)
        return f"{num1} {symbol} {num2} = {result}"
    except ValueError as e:
        return f"Error: {e}"

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("SIMPLE CALCULATOR")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)

def calculator():
    """Main calculator function"""
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nSelect operation (1-5): "))
            
            if choice == 5:
                print("\nThank you for using the calculator. Goodbye!")
                break
            
            if choice < 1 or choice > 5:
                print("Invalid choice! Please select 1-5.")
                continue
            
            print("\nEnter two numbers:")
            num1 = get_valid_number("First number: ")
            num2 = get_valid_number("Second number: ")
            
            result = perform_calculation(choice, num1, num2)
            print(f"\n✓ {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()
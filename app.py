def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to the test app.")

def add_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"The sum is: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def main():
    print("=== Simple Python Test Application ===")
    
    greet_user()
    
    while True:
        print("\nOptions:")
        print("1. Add two numbers")
        print("2. Exit")
        
        choice = input("Choose an option (1 or 2): ")
        
        if choice == "1":
            add_numbers()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
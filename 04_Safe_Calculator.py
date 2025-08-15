def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def show_menu():
    print("\n--- Safe Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

while True:
    show_menu()
    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:  # fixed integer check
            print("Exiting the calculator. Thank you!")
            break

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please enter a valid option.")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print("Goodbye!")

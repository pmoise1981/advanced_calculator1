import logging
from app.calculator import Calculator
from app.history import History

# Setup logging
logging.basicConfig(level=logging.INFO)

# Initialize History and Calculator
history = History("history.csv")
calculator = Calculator()

def get_float_input(prompt):
    """Helper function to get a valid float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function for the calculator."""
    print("Welcome to the Advanced Calculator")
    while True:
        try:
            print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. History\n6. Exit")
            choice = input("Please select an option: ")

            if choice == "1":
                x = get_float_input("Enter first number: ")
                y = get_float_input("Enter second number: ")
                result = calculator.add(x, y)
                print(f"Result: {result}")
                history.add_entry("add", x, y, result)

            elif choice == "2":
                x = get_float_input("Enter first number: ")
                y = get_float_input("Enter second number: ")
                result = calculator.subtract(x, y)
                print(f"Result: {result}")
                history.add_entry("subtract", x, y, result)

            elif choice == "3":
                x = get_float_input("Enter first number: ")
                y = get_float_input("Enter second number: ")
                result = calculator.multiply(x, y)
                print(f"Result: {result}")
                history.add_entry("multiply", x, y, result)

            elif choice == "4":
                x = get_float_input("Enter first number: ")
                y = get_float_input("Enter second number: ")
                try:
                    result = calculator.divide(x, y)
                    print(f"Result: {result}")
                    history.add_entry("divide", x, y, result)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "5":
                history_data = history.view_history()
                if history_data.empty:
                    print("No history found.")
                else:
                    print("History:")
                    print(history_data)

            elif choice == "6":
                print("User exited the calculator.")
                logging.info("User exited the calculator.")
                break  # Break out of the REPL loop

            else:
                print("Invalid choice. Please try again.")  # Handles invalid menu choice

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            logging.exception("An unexpected error occurred.")  # Log the actual exception

if __name__ == "__main__":
    main()


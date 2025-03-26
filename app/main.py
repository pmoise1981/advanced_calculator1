import sys
from app.calculator import Calculator
from app.history import History
from app.logger import logger

class REPL:
    """Command-Line Interface for the calculator."""

    def __init__(self):
        self.history = History()
        self.calculator = Calculator()
        self.commands = {
            "add": self.calculator.add,
            "sub": self.calculator.subtract,
            "mul": self.calculator.multiply,
            "div": self.calculator.divide,
            "history": self.show_history,
            "clear": self.clear_history,
            "exit": self.exit_repl
        }

    def run(self):
        print("Advanced Calculator - Type 'exit' to quit")
        while True:
            try:
                user_input = input(">> ").strip().split()
                if not user_input:
                    continue
                command = user_input[0].lower()
                if command in self.commands:
                    if command in ["history", "clear", "exit"]:
                        self.commands[command]()
                    else:
                        self.process_command(command, user_input[1:])
                else:
                    print("Unknown command.")
            except Exception as e:
                logger.error(f"Error: {e}")

    def process_command(self, command, args):
        if len(args) != 2:
            print("Error: Provide two numbers.")
            return
        try:
            a, b = map(float, args)
            result = self.commands[command](a, b)
            print(f"Result: {result}")
            self.history.add_entry(command, a, b, result)
        except ValueError:
            print("Error: Invalid input.")

    def show_history(self):
        print(self.history.history)

    def clear_history(self):
        self.history.clear_history()
        print("History cleared.")

    def exit_repl(self):
        print("Exiting calculator.")
        sys.exit()

if __name__ == "__main__":
    REPL().run()


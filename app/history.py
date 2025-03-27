import pandas as pd
import logging

# Assuming logger is already set up earlier
logger = logging.getLogger(__name__)

class History:
    def __init__(self, file_path):
        self.FILE_PATH = file_path
        try:
            self.history = pd.read_csv(self.FILE_PATH)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])
            self.history.to_csv(self.FILE_PATH, index=False)

    def add_entry(self, operation, operand1, operand2, result):
        """Adds an entry to the history and logs it."""
        if operation == "divide" and operand2 == 0:
            logger.error("Error encountered: division by zero")
            raise ZeroDivisionError("division by zero")  # Ensure ZeroDivisionError is raised

        try:
            new_entry = pd.DataFrame([[operation, operand1, operand2, result]], columns=self.history.columns)
            self.history = pd.concat([self.history, new_entry], ignore_index=True)
            self.history.to_csv(self.FILE_PATH, index=False)

            logger.info(f"Added history entry: {operation} {operand1} {operand2} = {result}")

            if operation == "subtract":
                logger.warning("Warning: Operation near completion.")  # Simulating a warning log

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise e

    def view_history(self):
        """Returns the history of operations."""
        return self.history  # Return the entire history DataFrame

    def display_history(self):
        """Displays the history in a user-friendly format."""
        print("History:")  # Ensure this part is printed regardless of history content
        if self.history.empty:
            print("No history found.")
        else:
            print(self.history.to_string(index=False))  # Pretty print without the index


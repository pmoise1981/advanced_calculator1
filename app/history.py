import pandas as pd

class History:
    """Handles calculation history using Pandas."""

    FILE_PATH = "history.csv"

    def __init__(self):
        self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])

    def add_entry(self, operation, operand1, operand2, result):
        new_entry = pd.DataFrame([[operation, operand1, operand2, result]], columns=self.history.columns)
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.history.to_csv(self.FILE_PATH, index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])
        self.history.to_csv(self.FILE_PATH, index=False)


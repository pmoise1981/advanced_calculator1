def add_entry(self, operation, operand1, operand2, result):
    """Adds an entry to the history and logs it."""
    new_entry = pd.DataFrame([[operation, operand1, operand2, result]], columns=self.history.columns)
    self.history = pd.concat([self.history, new_entry], ignore_index=True)
    self.history.to_csv(self.FILE_PATH, index=False)  # Ensure the history is written to the file
    print(self.history)  # Add this line to see the updated DataFrame
    # Log the operation added
    logger.info(f"Added history entry: {operation} {operand1} {operand2} = {result}")


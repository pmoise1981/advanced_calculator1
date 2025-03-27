Advanced Python Calculator for Software Engineering Graduate Course
📌 Project Overview
This midterm project requires developing an advanced Python-based calculator application that follows professional software development practices.

✨ Key Features & Requirements
✔ Command-Line Interface (REPL): Users interact with the calculator in real time.
✔ Design Patterns: Implementation of Command, Facade, Factory, Singleton, and Strategy patterns.
✔ Comprehensive Logging: Uses logging to track operations, errors, and debug messages dynamically configured via environment variables.
✔ Calculation History Management: Uses pandas to save, load, and manipulate history.
✔ Exception Handling: Demonstrates Look Before You Leap (LBYL) and Easier to Ask for Forgiveness than Permission (EAFP).
✔ Plugin System: Allows dynamic loading of new features.
✔ 95%+ Test Coverage: All critical functionalities are covered with pytest.
✔ GitHub Actions CI/CD: Runs tests automatically to ensure stability.


## Installation
To install the necessary dependencies, run:

```bash
pip install -r requirements.txt

# Usage
Run the calculator using:
python3 app/main.py

To run the test suite:
pytest --cov=app tests/

Video
https://drive.google.com/file/d/1GV9SIFVXowXs6gLiLPBNzC1waC5AUySP/view?usp=drive_link

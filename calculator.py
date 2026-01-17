import json
import os

HISTORY_FILE = "history.json"

# Load persistent history safely
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # File exists but is empty or corrupted
        return []

# Save history to non-volatile storage
def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def main():
    history = load_history()

    print("Calculator")
    while True:
        #SELECTING OPERATION
        print("Select an Operation:")
        print("(1) Addition")
        print("(2) Subtraction")
        print("(0) Quit")

        myInput : int
        while True:
            myInput = int(getInputNumber("> "))
            if myInput >= 0 and myInput < 3: break
            print("Please choose a number from 1 to 2.")
        
        if myInput == 0: break

        firstNumber = getInputNumber("Enter first number: ")
        secondNumber = getInputNumber("Enter second number: ")
        result = 0
        operation = 0

        match myInput:
            case 1:
                operation = "addition"
                result = add(firstNumber, secondNumber)
                print(f"Result: {result}")
            case 2:
                operation = "subtraction"
                result = subtract(firstNumber, secondNumber)
                print(f"Result: {result}")
            case 0: break
            case _: print("Error") #A Choice not corresponding to any operation

        history.append({
            "operation" : operation,
            "a" : firstNumber,
            "b" : secondNumber,
            "result" : result
        })
        save_history(history)
    
    print("Calculator closed. History saved.")

def getInputNumber(prompt) -> float:
    while True:
        try: return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.\n")

# ADDITION FUNCTION (AT THE BOTTOM)
def add(a, b):
    return a + b

# SUBTRACTION
def subtract(a, b):
    return a - b

if __name__ == "__main__":
    main()

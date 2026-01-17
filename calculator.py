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
        print("Choose an Operation:")
        print("(1) Addition")
        print("(2) Subtraction")
        print("(3) Multiplication")
        print("(0) Quit")

        myInput : int
        while True:
            myInput = int(getInputNumber("> "))
            if myInput >= 0 and myInput < 3: break
            print("Please choose a number from 0 to 3.")
        
        if myInput == 0: break

        a = getInputNumber("Enter first number: ")
        b = getInputNumber("Enter second number: ")
        result = 0
        operation_name = 0

        match myInput:
            case 1:
                operation_name = "addition"
                result = add(a, b)
                print(f"Result: {result}")
            case 2:
                operation_name = "subtraction"
                result = subtract(a, b)
                print(f"Result: {result}")
            case 3:
                operation_name = "multiplication"
                result = multiply(a, b)
                print(f"Result: {result}")
            case 0: break
            case _:
                print("Error") #A Choice not corresponding to any operation
                continue

        history.append({
            "operation" : operation_name,
            "a" : a,
            "b" : b,
            "result" : result
        })
        save_history(history)
    
    print("Calculator closed. History saved.")

def getInputNumber(prompt):
    while True:
        try: return float(input(prompt))
        except: print("Please enter a number.")

# ADDITION FUNCTION
def add(a, b):
    return a + b

# SUBTRACTION FUNCTION
def subtract(a, b):
    return a - b

# MULTIPLICATION FUNCTION
def multiply(a, b):
    return a * b

if __name__ == "__main__":
    main()

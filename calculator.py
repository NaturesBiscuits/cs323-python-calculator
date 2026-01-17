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
    print("Choose an operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("Type 'q' to quit\n")

    while True:
        choice = input("Select operation (1/2): ")
        if choice.lower() == "q":
            break

        if choice not in ("1", "2"):
            print("Invalid choice. Please select 1 or 2.\n")
            continue

        first = input("Enter first number: ")
        if first.lower() == "q":
            break

        second = input("Enter second number: ")
        if second.lower() == "q":
            break

        try:
            a = float(first)
            b = float(second)

            if choice == "1":
                result = add(a, b)
                operation_name = "addition"
            else:
                result = subtract(a, b)
                operation_name = "subtraction"

            print(f"Result: {result}\n")

            history.append({
                "operation": operation_name,
                "a": a,
                "b": b,
                "result": result
            })

            save_history(history)

        except ValueError:
            print("Invalid input. Please enter numbers.\n")

    print("Calculator closed. History saved.")

# ADDITION FUNCTION
def add(a, b):
    return a + b

# SUBTRACTION FUNCTION
def subtract(a, b):
    return a - b

if __name__ == "__main__":
    main()

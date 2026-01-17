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
    print("Type 'q' to quit\n")

    while True:
        first = input("Enter first number: ")
        if first.lower() == "q":
            break

        second = input("Enter second number: ")
        if second.lower() == "q":
            break

        try:
            a = float(first)
            b = float(second)
            result = add(a, b)

            print(f"Result: {result}\n")

            history.append({
                "operation": "addition",
                "a": a,
                "b": b,
                "result": result
            })

            save_history(history)

        except ValueError:
            print("Invalid input. Please enter numbers.\n")

    print("Calculator closed. History saved.")

# ADDITION FUNCTION (AT THE BOTTOM)
def add(a, b):
    return a + b

if __name__ == "__main__":
    main()

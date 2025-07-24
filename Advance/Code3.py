def main():
    print("Simple Command Line Calculator")
    print("Available operations: +, -, *, /")
    
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    
    while True:
        try:
            expr = input("Enter calculation (e.g., 2 + 3) or 'q' to quit: ")
            if expr.lower() == 'q':
                print("Goodbye!")
                break
            parts = expr.split()
            if len(parts) != 3:
                print("Invalid input format. Use: number operator number")
                continue
            x, op, y = parts
            x = float(x)
            y = float(y)
            if op in operations:
                result = operations[op](x, y)
                print("Result:", result)
            else:
                print("Unsupported operator.")
        except ValueError:
            print("Invalid numbers. Please enter valid numbers.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()

def main():
    print("Welcome to the Python Command-Line Tool!")
    print("Type 'help' to see available commands or 'exit' to quit.\n")

    while True:
        cmd = input("Enter command: ").strip().lower()

        # Exit command
        if cmd == "exit":
            print("Exiting the tool. Goodbye!")
            break

        # Help command
        elif cmd == "help":
            print("""
Available Commands:
- help : Show this help message.
- exit : Exit the program.
- print : Print a message. Example: print Hello World
- add : Add two numbers. Example: add 5 10
- multiply : Multiply two numbers. Example: multiply 4 6
            """)

        # Print command
        elif cmd.startswith("print"):
            _, *message = cmd.split(" ")
            print(" ".join(message))

        # Add command
        elif cmd.startswith("add"):
            try:
                _, num1, num2 = cmd.split(" ")
                result = float(num1) + float(num2)
                print(f"Result: {result}")
            except ValueError:
                print("Usage: add <num1> <num2> (e.g., add 5 10)")

        # Multiply command
        elif cmd.startswith("multiply"):
            try:
                _, num1, num2 = cmd.split(" ")
                result = float(num1) * float(num2)
                print(f"Result: {result}")
            except ValueError:
                print("Usage: multiply <num1> <num2> (e.g., multiply 4 6)")

        # Unknown command
        else:
            print(f"Unknown command: {cmd}. Type 'help' for available commands.")


# Run the main function
if __name__ == "__main__":
    main()
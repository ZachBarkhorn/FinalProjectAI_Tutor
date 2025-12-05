#Interface for interaction with the GPT model

import sys
from tutor import (
    explain_concept,
    debug_code,
    generate_example,
    create_exercise,
    evaluate_answer
)

def print_menu():
    print("\nAI Python Tutor")
    print("1. Explain a concept")
    print("2. Debug code")
    print("3. Generate an example")
    print("4. Create an exercise")
    print("5. Evaluate an answer")
    print("6. Exit")

def get_multiline_input(user_direction):
    
    #Reads multi-line input from the user.
    #Finish input with Ctrl+Z + Enter (Windows) or Ctrl+D (Mac/Linux).
    
    print(user_direction)
    user_input = sys.stdin.read().strip()
    # Remove trailing ^Z or Ctrl+Z characters and extra whitespace
    return user_input.rstrip("\x1a").strip() #\x1a is the ASCII code for Ctrl+Z character

def main():
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            topic = get_multiline_input("Enter a Python topic or concept (finish with Ctrl+Z + Enter):")
            print("\n=== Explanation ===\n")
            explain_concept(topic)

        elif choice == "2":
            code = get_multiline_input("Paste your Python code (finish with Ctrl+Z + Enter):")
            print("\n=== Debugging Suggestions ===\n")
            print(debug_code(code))

        elif choice == "3":
            topic = get_multiline_input("Enter a topic to generate a Python example (finish with Ctrl+Z + Enter):")
            print("\n=== Generated Example ===\n")
            print(generate_example(topic))

        elif choice == "4":
            topic = get_multiline_input("Enter a topic for a beginner exercise (finish with Ctrl+Z + Enter):")
            print("\n=== Generated Exercise ===\n")
            print(create_exercise(topic))

        elif choice == "5":
            problem = get_multiline_input("Enter the exercise/problem description (finish with Ctrl+Z + Enter):")
            answer = get_multiline_input("Enter the student's answer (finish with Ctrl+Z + Enter):")
            print("\n=== Evaluation ===\n")
            print(evaluate_answer(problem, answer))

        elif choice == "6":
            print("Exiting AI Tutor. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()

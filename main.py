#Interface for interaction with the GPT model

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


def main():
    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            topic = input("Enter a Python topic: ")
            print(explain_concept(topic))

        elif choice == "2":
            code = input("Paste your Python code:\n")
            print(debug_code(code))

        elif choice == "3":
            topic = input("Enter a topic: ")
            print(generate_example(topic))

        elif choice == "4":
            topic = input("Enter a topic: ")
            print(create_exercise(topic))

        elif choice == "5":
            problem = input("Enter the problem/exercise: ")
            answer = input("Enter the student's answer:\n")
            print(evaluate_answer(problem, answer))

        elif choice == "6":
            break

        else:
            print("Invalid choice. Try again.")


    if __name__ == "__main__":
        main()

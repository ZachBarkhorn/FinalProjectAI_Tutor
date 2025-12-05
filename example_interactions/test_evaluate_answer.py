from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tutor import evaluate_answer

INTERACTIONS_DIR = "example_interactions"
os.makedirs(INTERACTIONS_DIR, exist_ok=True)

if __name__ == "__main__":
    sample_exercise = "Write a loop to sum the elements in a list."
    student_answer = "total = sum([1,2,3])"
    prompt = f"Exercise: {sample_exercise}\nStudent Answer: {student_answer}"
    print("\n🔹 Evaluate Answer\n")
    response = evaluate_answer(sample_exercise, student_answer)

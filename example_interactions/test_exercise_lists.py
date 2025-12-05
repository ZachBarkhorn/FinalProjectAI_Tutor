from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tutor import create_exercise

INTERACTIONS_DIR = "example_interactions"
os.makedirs(INTERACTIONS_DIR, exist_ok=True)

if __name__ == "__main__":
    prompt = "Create a beginner Python exercise on lists."
    print("\n🔹 Generate Exercise: lists\n")
    response = create_exercise("lists")


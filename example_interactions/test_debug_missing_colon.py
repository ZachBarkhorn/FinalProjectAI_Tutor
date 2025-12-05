from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tutor import debug_code

INTERACTIONS_DIR = "example_interactions"
os.makedirs(INTERACTIONS_DIR, exist_ok=True)


if __name__ == "__main__":
    sample_code = "for i in range(3)\n    print(i)"
    prompt = f"Debug the following Python code:\n{sample_code}"
    print("\n🔹 Debug Code: missing colon\n")
    response = debug_code(sample_code)

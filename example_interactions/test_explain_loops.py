import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tutor import explain_concept

INTERACTIONS_DIR = "example_interactions"
os.makedirs(INTERACTIONS_DIR, exist_ok=True)



if __name__ == "__main__":
    prompt = "Explain the Python concept 'loops' to a beginner with step-by-step examples."
    print("🔹 Explain Concept: loops\n")
    response = explain_concept("loops")

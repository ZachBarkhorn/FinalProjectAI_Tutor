# prompts.py

#prompt to set the personality and role of the AI tutor
SYSTEM_PROMPT = """
You are an AI tutor for beginner Python programmers.
Explain concepts clearly and step by step.
Provide examples when needed.
If code has errors, debug and explain the errors.
Always be friendly and encouraging.
"""

#prompt to debug user code with clear parameters to help the user learn
DEBUG_PROMPT = """
The user wrote this Python code:

{user_code}

Check the code for errors.
Explain each error in simple terms.
Provide a corrected version of the code.
"""

#prompt to create beginner level python exercises with clear parameters
EXERCISE_PROMPT = """
Create a beginner Python exercise.
Include:
- Problem description
- Example input/output
- Difficulty level (easy)
"""

#prompt to evaluate user answer and help them improve
EVALUATION_PROMPT = """
The user submitted this answer:

{user_answer}

Check if it correctly solves the problem:

{exercise_description}

Give feedback on what is correct, what is wrong, and hints for improvement.
"""

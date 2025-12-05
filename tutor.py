import openai
from prompts import SYSTEM_PROMPT, DEBUG_PROMPT, EXERCISE_PROMPT, EVALUATION_PROMPT

#central API call to interact with gpt model and produce responses to user input
def call_ai(prompt, temperature=0.7):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=800
    )
    return response.choices[0].message['content'].strip()

#prompt to the API to explain a beginner python concept to a learning programmer
#moderate temperature to allow for some creativity in explanations
def explain_concept(topic):
    prompt = f"Explain the Python concept '{topic}' to a beginner with step-by-step examples."
    return call_ai(prompt, temperature=0.5)


#uses the debug prompt to check for user code errors and provide corrections with limitations on how advanced the corrections can be
#low temperature to ensure accurate debugging
def debug_code(code):
    prompt = DEBUG_PROMPT.format(user_code=code)
    return call_ai(prompt, temperature=0.2)


#generates a simple pyton example to demonstrate the topic that the user is learning
#moderate temperature to allow for some creativity in example generation
def generate_example(topic):
    prompt = f"Generate a simple Python example that demonstrates: {topic}"
    return call_ai(prompt, temperature=0.6)


#uses the exercise prompt to create a beginner level python exercise for the user to practice on
#high temperature for increased creativity in exercise production
def create_exercise(topic):
    prompt = EXERCISE_PROMPT.format(topic=topic)
    return call_ai(prompt, temperature=0.9)


#uses the evaluation prompt to assess the user's input and provide them guidance on how they can improve their answer
#Low temperature to ensure a factual thought process from the model
def evaluate_answer(problem, answer):
    prompt = f"{problem}\n\nStudent answer:\n{answer}\n\nEvaluate correctness and give feedback."
    return call_ai(prompt, temperature=0.3)

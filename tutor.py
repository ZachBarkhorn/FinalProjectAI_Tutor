import os
from datetime import datetime
import json

from ollama import Client
from prompts import SYSTEM_PROMPT, DEBUG_PROMPT, EXERCISE_PROMPT, EVALUATION_PROMPT

client = Client(
    host='https://ollama.com',
    #Bearer indicates that whoever holds the api key has access
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
)

#central API call to interact with gpt model and produce responses to user input
def call_ai(prompt, save_json=True):
    messages = [
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': prompt}
    ]

    response_text = ""
    final_metrics = {}

    # Streaming call
    for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
        if part.message:  # partial content
            print(part.message.content, end="", flush=True)  # live typing effect
            response_text += part.message.content

        # Capture metrics from final chunk only
        if getattr(part, "done", False):
            total_duration_ns = getattr(part, "total_duration", 0)
            final_metrics = {
                "total_duration_s": total_duration_ns / 1e9,  # convert ns -> s
                "prompt_eval_count": getattr(part, "prompt_eval_count", 0),
                "eval_count": getattr(part, "eval_count", 0),
                "tokens_per_second": getattr(part, "eval_count", 0) / (total_duration_ns / 1e9) if total_duration_ns > 0 else 0
            }

    print()  # newline after streaming

    # Save JSON if requested
    if save_json:
        analysis_data = {
            "prompt": prompt,
            "response": response_text,
            "metrics": final_metrics,
            "timestamp": datetime.now().isoformat()
        }
        filename = f"logs/ai_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(analysis_data, f, indent=4)
        print(f"\nAnalysis saved to {filename}")


#prompt to the API to explain a beginner python concept to a learning programmer
#moderate temperature to allow for some creativity in explanations
def explain_concept(topic):
    prompt = f"Explain the Python concept '{topic}' to a beginner with step-by-step examples."
    return call_ai(prompt)



#uses the debug prompt to check for user code errors and provide corrections with limitations on how advanced the corrections can be
#low temperature to ensure accurate debugging
def debug_code(code):
    prompt = DEBUG_PROMPT.format(user_code=code)
    return call_ai(prompt)


#generates a simple pyton example to demonstrate the topic that the user is learning
#moderate temperature to allow for some creativity in example generation
def generate_example(topic):
    prompt = f"Generate a simple Python example that demonstrates: {topic}"
    return call_ai(prompt)


#uses the exercise prompt to create a beginner level python exercise for the user to practice on
#high temperature for increased creativity in exercise production
def create_exercise(topic):
    prompt = EXERCISE_PROMPT.format(topic=topic)
    return call_ai(prompt)


#uses the evaluation prompt to assess the user's input and provide them guidance on how they can improve their answer
#Low temperature to ensure a factual thought process from the model
def evaluate_answer(problem, answer):
    prompt = EVALUATION_PROMPT.format(
        exercise_description=problem,
        user_answer=answer
    )
    return call_ai(prompt)

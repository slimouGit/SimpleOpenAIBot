import openai

from config import API_KEY
from prompt import PROMPT

openai.api_key = API_KEY
messages = [{"role": "system", "content":
    "You are a intelligent assistant."}]
global_prompt = PROMPT

def print_hi(name):
    print(f'Welcome to {name}')


def chatGPT(text, temperature=0.7):
    messages = [{"role": "system", "content": "You are a fraud detection assistant."}]

    messages.append({"role": "user", "content": global_prompt + text})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=temperature
    )

    reply = chat.choices[0].message['content']
    return reply


if __name__ == '__main__':
    while True:
        text_to_check = input("Enter the text to check (or 'exit' to quit): ")
        if text_to_check.lower() == 'exit':
            break

        response = chatGPT(text_to_check, temperature=0.8)
        print(f"Response: {response}")

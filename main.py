import openai

from config import API_KEY

openai.api_key = API_KEY
messages = [ {"role": "system", "content":
              "You are a intelligent assistant."} ]

def print_hi(name):
    print(f'Welcome to {name}')

def chatGPT():
    while True:
        message = input("Your question : ")
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})

if __name__ == '__main__':
    print_hi('OpenAI')
    chatGPT()




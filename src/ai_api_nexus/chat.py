from client import client as cl # type: ignore
from config import AI_MODEL # type: ignore
# from ai_api_nexus.curse.schemas import QuizSchema

messages = [
    # {"role": "system", "content": "answer strictly in this form: [{'analysis': 'text'}, {'answer': 'text'}]"},
    # {"role": "user", "content": ReturnSchema}
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "/exit":
        break

    messages.append({"role": "user", "content": user_input})
    
    
    response = cl.chat.completions.create(
        model=AI_MODEL,
        messages=messages
    )

    bot_reply = response.choices[0].message.content
    print(f"Бот: {bot_reply}\n")

    messages.append({"role": "assistant", "content": bot_reply})
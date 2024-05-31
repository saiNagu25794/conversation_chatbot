from groq import Groq

import re

import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

async def qroq_response(question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content


async def convert_text_to_messages(text):
    messages = []
    # Split text into messages based on "Human:" and "AI:" tags
    message_blocks = re.split(r'(Human:|AI:)', text)[1:]

    for i in range(0, len(message_blocks), 2):
        speaker = message_blocks[i].strip()
        text = message_blocks[i + 1].strip()
        messages.append({"person": speaker[0:len(speaker) - 1], "text": text})
    return messages



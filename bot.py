import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def prompt(prompt):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content
from pydantic import BaseModel
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CalendarEvent(BaseModel):
    name: str
    day: str
    participants: list[str]
    date: str


completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "schedule a meeting with John and Jane on Monday which is on feb 12th 2025"},
    ],
    response_format=CalendarEvent
)

event=completion.choices[0].message.parsed
print(event.name)
print(event.day)
print(event.date)
print(event.participants)
import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_email(subject: str, body: str, category: str, priority: str) -> dict:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"""
            Analyze this email and respond in JSON format only, no extra text:
            {{
                "summary": "2-3 sentence summary",
                "action_items": ["item1", "item2"],
                "suggested_reply": "brief reply"
            }}

            Subject: {subject}
            Category: {category}
            Priority: {priority}
            Body: {body}
        """}],
        temperature=0.3
    )

    text = response.choices[0].message.content.strip()
    text = text.replace("```json", "").replace("```", "")
    return json.loads(text)

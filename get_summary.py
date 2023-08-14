import openai
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

question = """
Write a new title. (Will be used later to place the jobs in categories).
Write a short summary about this role for a developer. 

What are the requirements?
What languages?
What frameworks?
How many years experience is needed? If there isnt a number in the description, estimate one.
How senior is this role on a scale 1-100.

What is the email where you could send a resume? (If mentioned)

Reply with JSON format.
"""

def call_chatGPT(prefix, job):
    text = {"role": "user", "content": prefix + job}

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }
    data = {
        "model": "gpt-4",
        "messages": [text],
        "temperature": 0.7,
    }
    chatGPT_response = requests.post(url, headers=headers, data=json.dumps(data))
    content = chatGPT_response.json()["choices"][0]["message"]["content"]

    return content

with open('jobs.json', 'r', encoding='utf-8') as f:
    jobs = json.load(f)

# Convert dict into string
job = json.dumps(jobs[0])

answer = call_chatGPT(question, job)

print(answer)
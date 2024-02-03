import google.generativeai as genai 
import os 
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv('Gemini_API_key'))
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
response = chat.send_message([
    "who is God ?",
    #img
], stream=True)

for chunk in response:
    print(chunk.text, end= "")
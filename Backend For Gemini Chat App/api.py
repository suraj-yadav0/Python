import io 
import json
import os 
from typing import List
import PIL.Image
import google.generativeai as genai 
from dotenv import load_dotenv
from fastapi import FastAPI , WebSocket

load_dotenv()
genai.configure(api_key=os.getenv('Gemini_API_key'))
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


api = FastAPI()

@app.WebSocket("/ws")
async def websocket_endpoint()
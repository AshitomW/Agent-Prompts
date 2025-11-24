from openai import OpenAI
from dotenv import load_dotenv
import os 
load_dotenv()

API_KEY = os.getenv("GEMINI_KEY")
API_URL = os.getenv("GEMINI_URL")

client = OpenAI(
  api_key=API_KEY,
  base_url=API_URL
)



SYSTEM_PROMPT = """
  You are an AI Persona Assitant name Humba. 
  You are acting on behalf of Humba Rumba who is a teen tech enthusiast. Your main tech stack is typescript and python.
  You are currently learning Generative AI these days:

  Examples: 

  Question: Hey 
  Answer: Hey! Humba Here , What's Cooking.

  Question: What is generative ai?
  Answer: Generative AI (Gen AI) is a type of artificial intelligence that can create new content.
            Instead of just recognizing patterns, it produces things — like:

            text (like me talking to you rn)

            images (Midjourney, DALL·E)

            audio (AI song covers)

            video (Sora-type models)

            code (Copilot, GPT-Coder)

            3D models, music, etc.
  
"""



response = client.chat.completions.create(
  model="gemini-2.5-flash",
  messages=[
    {"role":"system","content":SYSTEM_PROMPT},
    {"role":"user","content":"Hey There"}
    
  ]
)
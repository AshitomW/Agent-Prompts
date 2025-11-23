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


# Give Examples Along With Instructions.



SYSTEM_PROMPT = """ 
You should only answer coding related questions. Do not answer anything else. Any Questions other than coding should be discarded and just say sorry.

Rules: 

  - Strictly follow the ouput in JSON Format: 
    {{
     "code":"string" or Null,
     "isCodingQuestion":boolean
    }}

Examples: 

Question: Can you explain the a + b whole cube expansion?
Answer: {{"code":null,isCodingQuestion:false}}

Question: Write a code in python for adding two numbers.
Answer: 
  {{
    "code":"add_two = lambda a,b: a+b",
    "isCodingQuestion":  true,
  }}

"""

response = client.chat.completions.create(
  model="gemini-2.5-flash",
  messages=[
    {"role":"system","content":SYSTEM_PROMPT},
    {"role":"user","content":"Hello"}
    
  ]
)

print(response.choices[0].message.content)


# Few shot prompting : Model is provided with a few examples before asking it to generate a response.
# Use more examples , generally given more than 50 , 60 or higher.
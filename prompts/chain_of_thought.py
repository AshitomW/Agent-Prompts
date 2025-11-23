from openai import OpenAI
from dotenv import load_dotenv
import os 
import json

load_dotenv()

API_KEY = os.getenv("GEMINI_KEY")
API_URL = os.getenv("GEMINI_URL")

client = OpenAI(
  api_key=API_KEY,
  base_url=API_URL
)


SYSTEM_PROMPT = """
  You're an expert AI Assistant in resolving user queries using chain of thought.
  You work on START, PLAN and OUTPUT Steps.
  You need to first PLAN what needs to be done. The plan can be multiple steps.
  Once you think enough plan has been done, finally you can give an OUTPUT.


  Rules: 

  - Strictly Follow the given JSON output format
  - Only run one step at a time
  - The sequence of steps is START (where user gives an input) , PLAN (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user.)


  Output Format: 

  {{
    "step":"start" | "plan" | "output",
    "content":"string"
  }}


  Examples:

  START: Hey , can you solve 2 + 3 *4 / 10
  PLAN: {"step":"plan", "content":"Seems like user is interested in maths problem"},
  PLAN: {"step:"plan","content":"Looking at the problem, we shodl solve this using the BODMAS method"},
  PLAN: {"step":"plan", "content":"Yes, the bodmas method is appropriate rule for this expression"},
  PLAN: {"step":"plan", "content":"First we should multiply 3 and 4 which is 12"},
  PLAN: {"step":"plan", "content":"Now the new equation is 2 + 12 / 10"},
  PLAN: {"step":"plan", "content":"Now we should perform division on 12 / 10 which results in 1.2"},
  PLAN: {"step":"plan", "content":"Now the resulting equation is 2 + 1.2"},
  PLAN: {"step":"plan", "content":"Now performing  addtion of 2 + 1.2 we get 3.2"},
  PLAN: {"step":"plan", "content":"since there are no more operations to be done , the final result is 3.2"},
  OUTPUT: {"step":"output", "content":"2 + 3 * 4 / 10 = 3.2 "},


  
  

"""




response = client.chat.completions.create(
  model="gemini-2.5-flash",
  response_format={"type":"json_object"},
  messages=[
    {"role":"system","content":SYSTEM_PROMPT},
    {"role":"user","content":"Hey, write a code to add n numbers in js"},
    # Manually Adding to history
    {"role":"assistant","content": json.dumps(
        {
          "step": "plan",
          "content": "The user wants a JavaScript function to add 'n' numbers. I should define a function that can accept a variable number of arguments."
        }
    )}
    ,
     {"role":"assistant","content": json.dumps(
            {
        "step": "plan",
        "content": "To add 'n' numbers in JavaScript, I can define a function that utilizes the rest parameter syntax (`...numbers`) to accept an arbitrary number of arguments. Then, I will iterate through these numbers (e.g., using `reduce` or a `for...of` loop) and sum them up."
      }
    )}
  ]
)

print(response.choices[0].message.content)


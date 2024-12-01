import streamlit as st
import google.generativeai as ai
from dotenv import load_dotenv 
import os 

st.title("Code Review by :blue[AI] 📜")

user_prompt = st.text_area("Get your code fixed:", placeholder="Write your code...")
btn_click = st.button("Get Review")

load_dotenv(dotenv_path="googleapi.env") 
ai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

sys_prompt = "You are a programming code reviewer for programming languages like Python, JavaScript, Java, etc. Check if the provided code is correct. You should provide a code review with bug report, fixes and accurate code. Provide the output, time and space complexities of the program."

model = ai.GenerativeModel(model_name="gemini-1.5-flash-002",system_instruction=sys_prompt)

if btn_click == True:
    response = model.generate_content(user_prompt)
    st.write(response.text)
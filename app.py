import streamlit as st
from PIL import Image
from dotenv import load_dotenv 
import os
import io
import google.generativeai as ai
from google.cloud import texttospeech
from google.cloud import vision
from langchain_core.output_parsers import StrOutputParser

# title
st.title("Scene Recognition for Safety and Assistance")

# api configuration
load_dotenv(dotenv_path="googleapi.env") 
ai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

sys_prompt = "You will be provided an image and text as the input. You need to assess the image accurately. Observe the image and understand the input from selectbox to provide output for only the input selected in the selectbox. You will be helping individuals as they are in the scene of the image who has a very low vision to see."

input = st.selectbox("Choose one",("Textual Understanding of Image","Recognition of objects in the image", "Obstacle Detection in the image"),key="input")

uploaded_file = st.file_uploader(label = "Upload an Image...", type = ["jpeg", "jpg", "png"])


# define the Model and the Image Annotation
def generate_response(input, image):
    model = ai.GenerativeModel("gemini-1.5-flash", system_instruction=sys_prompt)
    if image != "":
        response = model.generate_content([input, image])
    return(response.text)

# Image Processing
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Image Uploaded", use_container_width = True)
    

submit = st.button("Get Results")

if submit:
    response = generate_response(input, image)
    st.subheader(f"{input}")
    st.write(response)


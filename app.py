# python --version
# python -m venv .venv
# .\.venv\Scripts\activate
# pip install streamlit langchain google-generativeai langchain-google-genai 
# running the project  'streamlit run app.py'
# git init
# pip freeze > requirements.text
# git add .
# git commit -m "first commit" (if email not configed "git config --global user.email "abhi.1593@gmail.com"")
# git remote add origin https://github.com/abhi-1593/movie-recommender.git
# git push -u origin main


# created the virtual environment using python -m venv .venv
# .\.venv\Scripts\activate
# Install the libraries - streamlit, google-generativeai, langchain
# pip install streamlit langchain google-generativeai
# install langchain-google-genai

import streamlit as st
import langchain
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Design the page - Title of the page
st.title("Movie Recommendor system using Google Gemini")
# st.subheader("Please enter the Movie Name")
user_input=st.text_input("Enter a Movie Title, genre or keywords (e.g.sci-fi movie)")

# LLM Model
# Prompt Template
demo_template='''Based on the input, here are some Movie Recomendations\
    for {user_input}:\n'''
template=PromptTemplate(input_variable=['user_input'],template=demo_template)

# Initialize the gemini-pro model
llms=ChatGoogleGenerativeAI(model="gemini-pro",api_key="AIzaSyDOsV6e2ZadNnHwC7YugCAhkRglayCTDPs")

# Generate the Recommendations when the user  provides input
if user_input:
    prompt=template.format(user_input=user_input)
    recommendations=llms.predict(text=prompt)
    st.write(f"Recommendations for you: \n{recommendations}")
else:
    st.write(" ")

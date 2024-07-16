import streamlit as st 
import os 
import string
from API import GROQ_API_KEY

def ai():
    from groq import Groq
    client=Groq(
        api_key=GROQ_API_KEY,
    )
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content":user_input,
        }
    ],
    model="llama3-70b-8192",)  
    st.write("GROQ:")
    st.write("👨‍🎤",chat_completion.choices[0].message.content)

st.title("MINEY🎭👨‍🎤🎬")
input = st.text_input("Enter your question")
#st.write("Top artist are:",'Jon snow',' Morgan freeman ',' Trevor noha ','Adam sandlers','Kevin Hart ',' Kenny Sebastian ',' Biswa Kalyan Rath ',' Kanan Gill')
character=st.text_input("Enter the characther that has to answer👨‍🎤:\t")
user_input=input+character


# Display the user input
st.write('👨‍💻:', user_input)
st.write(ai())

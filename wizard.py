import streamlit as st 
from groq import Groq
from typing import Generator
from GROQ_AI.API import GROQ_API_KEY


st.set_page_config(page_icon="🔮",layout='wide',page_title="WIZARD AI🧙‍♂️✨")
st.header("WIZARD AI✨")
def icon(emoji:str):
    st.write( f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
icon('🪄')

st.subheader("Powered by GroQ🤖 with Llama2🦙",divider='rainbow',anchor=False)
with st.sidebar:
    st.title('🧙‍♂️✨ WIZARD AI')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [GROQ](https://groq.com/)
    - [MY_Github👨‍💻](https://github.com/Girishgh7)
    ''')
    st.write('Made with magic of wizards and llms ❤️')
    st.write('Made by 🐒Girish_GH🤖')
    st.write('Powerd By GroQ cloud👨‍💻☁️ using llama2🦙')

client=Groq(
    api_key=GROQ_API_KEY
)
# Initialize chat history & selected model
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None


    # Display  history on app rerun
for message in st.session_state.messages:
    avatar = '🧙‍♂️' if message["role"] == "assistant" else '👨‍💻'
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    """Yield chat response content from the Groq API response."""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content


if prompt := st.chat_input("Enter your prompt here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user", avatar='👨‍💻'):
        st.markdown(prompt)
    try:
        chat_completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": m["role"],
                    "content": m["content"]
                }
                for m in st.session_state.messages
            ],
            max_tokens=30000,
            stream=True
        )
        with st.chat_message("assistant", avatar="🧙‍♂️"):
             chat_responses_generator = generate_chat_responses(chat_completion)
             full_response = st.write_stream(chat_responses_generator)
    except Exception as e:
        st.error(e, icon="🚨❌")

    # Append the full response to session_state.messages
    if isinstance(full_response, str):
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response})
    else:
        # Handle the case where full_response is not a string
        combined_response = "\n".join(str(item) for item in full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": combined_response})
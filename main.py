import asyncio

import streamlit as st
from langchain.memory import ConversationBufferWindowMemory

from html_code import title_html_code
from groq_code import qroq_response, convert_text_to_messages


async def main():
    st.markdown(await title_html_code(), unsafe_allow_html=True)

    with st.sidebar:
        conversational_memory_length = st.slider('Conversational memory length:', 1, 10, value=5)
        memory = ConversationBufferWindowMemory(k=conversational_memory_length)



    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    if user_question := st.chat_input(placeholder="Ask me anything"):
        response = await qroq_response(user_question)
        message = {'human': user_question, 'AI': response}
        st.session_state.chat_history.append(message)

    if "chat_history" in st.session_state:
        for message in st.session_state.chat_history:
            memory.save_context({'input': message['human']}, {'output': message['AI']})

    messages_text = memory.load_memory_variables({})['history']
    response = await convert_text_to_messages(messages_text)
    for message in response:
        st.write(f"<span style='font-size: 18px; font-weight: bold; color: red;'>{message['person']}</span>: {message['text']}"
                       , unsafe_allow_html=True)


if __name__ == "__main__":
    asyncio.run(main())

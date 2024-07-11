import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

def retrieve_information(query):
    # Simulating a retrieval function, replace with actual retrieval logic
    response = openai.Completion.create(
        engine="gpt-4o",
        prompt=f"Retrieve information about: {query}",
        max_tokens=200
    )
    return response.choices[0].text.strip()

def chat_with_openai(message):
    response = openai.Completion.create(
        engine="gpt-4o",
        prompt=message,
        max_tokens=200
    )
    return response.choices[0].text.strip()

def main():
    st.title("PFAS Chatbot")
    st.write("Welcome to the Chatbot! Ask me anything.")

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    user_input = st.text_input("You: ")

    if user_input:
        retrieved_info = retrieve_information(user_input)
        
        if retrieved_info:
            st.session_state.conversation.append(("You", user_input))
            st.session_state.conversation.append(("Bot (retrieved)", retrieved_info))
        else:
            bot_response = chat_with_openai(user_input)
            st.session_state.conversation.append(("You", user_input))
            st.session_state.conversation.append(("Bot", bot_response))

    for speaker, message in st.session_state.conversation:
        st.write(f"**{speaker}:** {message}")

if __name__ == "__main__":
    main()

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Initialize Gemini 1.5 Pro model
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", system_instruction="Resolve data science doubts with accurate and concise responses. Maximum 2-3 lines per completion.")


# Function to initialize session state variables
def init_session_state():
    st.session_state.chat_history = []

# Streamlit UI
def main():
    # Initialize session state variables
    if 'chat_history' not in st.session_state:
        init_session_state()

    st.title("Conversational AI Data Science Tutor")

    # User input
    user_input = st.text_input("Ask your data science question:")

    if st.button("Ask"):
        if user_input.strip() == "":
            st.error("Please enter a question.")
        else:
            # Process user question
            response = process_question(user_input)
            update_chat_history(user_input, response)
            st.write("Tutor:", response)

    # Display chat history
    st.subheader("Chat History")
    show_chat_history()

def process_question(question):
    # Generate response using Gemini 1.5 Pro model
    response = model.generate_content(question)
    return response.text

def update_chat_history(user_input, response):
    # Append user input and response to chat history
    st.session_state.chat_history.append((user_input, response))

def show_chat_history():
    # Display chat history in reverse order with latest conversation at the top
    # Exclude the last entered query from the chat history
    for user_input, response in reversed(st.session_state.chat_history[:-1]):
        st.write("User:", user_input)
        st.write("Tutor:", response)

if __name__ == "__main__":
    main()
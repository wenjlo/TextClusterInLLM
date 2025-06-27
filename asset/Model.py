from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cert/cdp-rd-vertex-ai.json'


chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17",temperature=0)


def classify_text(text):
    global chat_model
    messages = [
        (
            "system",
            "You are a customer service representative of an online gaming platform operator."
            "You will get a lot of questions from customers who operate online gaming platforms."
            "Your task is to find the summary of these questions (the summary should not exceed 10 words) Answer in Chinese"
        ),
        ("human", "The quesitons are : " + text),
    ]
    ai_msg = chat_model.invoke(messages)
    return ai_msg.content


embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07")
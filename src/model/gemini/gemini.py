from langchain_google_genai import ChatGoogleGenerativeAI
import os

def gemini():
    """Create and return a Gemini chat model instance"""
    model = ChatGoogleGenerativeAI(
        api_key=os.getenv("GOOGLE_API_KEY"), 
        model="gemini-2.0-flash",
        temperature=0
    )
    return model

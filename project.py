import os
from typing import TypedDict

#lets create the state first

class pipelinestate(TypedDict):
    raw_input : str
    edited_text : str
    sript_text : str
    final_output : str


from langchain_groq import ChatGroq
from dotenv import load_dotenv 

load_dotenv()
llm = chat_groq = ChatGroq(api_key=os.environ.get("GROQ_API_KEY"), model="llama-3.3-70b-versatile", temperature=0.7)

def editor_node(state: pipelinestate) -> dict:
    """Stage 1: Cleans up grammar, removes typos, and refines the tone."""
    prompt = (
        "you are an expert copyeditor. Clean up the following raw text."
    )
    edited_text = llm(prompt)
    state['edited_text'] = edited_text
    return state
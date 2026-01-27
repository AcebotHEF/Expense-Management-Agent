import pandas as pd
from expense_data import load_expenses
from expense_prompt import expense_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

def analyze_expenses():
    df = load_expenses()
    table = df.to_string(index=False)

    # CHANGED: Configure Gemini
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.0-flash", 
        temperature=0.2
    )
    
    prompt = expense_prompt.format(expense_table=table)
    
    # CHANGED: Use .invoke() instead of .predict()
    response = llm.invoke(prompt)
    
    return df, response.content
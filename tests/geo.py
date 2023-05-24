import pandas as pd
from langchain.chat_models import ChatOpenAI
import sayql

df = pd.read_csv('https://raw.githubusercontent.com/scpike/us-state-county-zip/master/geo-data.csv')

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

query = "What is the Zipcode of Clanton. AL?"
print(f"Query: {query}")

# Interface subject to change!
print("Resulting df:")
print(sayql.query("What is the Zipcode of Clanton. AL?", return_row=True, df = df, llm = llm))

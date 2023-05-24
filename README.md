# sayql
Talk to your data


# Installation
```pip install sayql```

# Usage

```
df = pd.read_csv('https://raw.githubusercontent.com/scpike/us-state-county-zip/master/geo-data.csv')

llm = OpenAIChat(model="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)

# Interface subject to change!
SayQL(df, llm).query("What is the Zipcode of Clanton. AL? Return the whole row")

>>>    state_fips    state state_abbr zipcode   county     city
0           1  Alabama         AL   35045  Chilton  Clanton
```
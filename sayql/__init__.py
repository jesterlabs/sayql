from sayql.sayql import SayQL

def query(
    query: str,
    df,
    llm = None,
    return_row: bool = True
):
    return SayQL(df, llm).query(query, return_row=return_row)

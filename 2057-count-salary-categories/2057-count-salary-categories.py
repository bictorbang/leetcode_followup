import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts["income"]= pd.cut(accounts["income"], bins = [0, 20000, 50001, float("inf")], labels = ["Low Salary", "Average Salary", "High Salary"], right = False)
    return pd.DataFrame(accounts["income"].value_counts().reset_index()).rename({"income": "category", "count" : "accounts_count"}, axis = 1)
#
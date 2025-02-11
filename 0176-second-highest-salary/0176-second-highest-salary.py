import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    e = employee[["salary"]].drop_duplicates()
    if len(e) < 2: return pd.DataFrame({"SecondHighestSalary" : [None]})
    return e.sort_values("salary", ascending = False).iloc[[1]].rename({"salary" : "SecondHighestSalary"}, axis = 1)
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 1 or N > len(e := employee[["salary"]].drop_duplicates()): return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    return e.sort_values(by = "salary", ascending = False).iloc[[N-1]].rename({"salary" : f"getNthHighestSalary({N})"}, axis = 1)
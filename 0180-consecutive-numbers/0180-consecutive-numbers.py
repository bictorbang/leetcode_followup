import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs["unique"] = logs["num"].rolling(window = 3).apply(lambda x: x.nunique())
    return logs[(logs["unique"] == 1)][["num"]].rename({"num" : "ConsecutiveNums"}, axis = 1).drop_duplicates()
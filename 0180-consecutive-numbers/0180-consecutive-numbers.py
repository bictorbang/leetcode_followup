import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    return logs[["num"]][(logs["num"] == logs["num"].shift()) & (logs["num"] == logs["num"].shift(2))].rename({"num" : "ConsecutiveNums"}, axis = 1).drop_duplicates()
    #return logs[["num"]].rename({"num": "ConsecutiveNums"}, axis = 1)[((logs == logs.shift()) & (logs == logs.shift(2)))].dropna()
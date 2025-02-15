import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium = stadium[stadium["people"] > 99]
    stadium["diff"] = stadium["id"].diff() 
    stadium["flag"] = (stadium["diff"] == 1) & (stadium["diff"].shift() == 1)
    return stadium.loc[stadium["flag"] | stadium["flag"].shift(-1) | stadium["flag"].shift(-2), ["id", "visit_date", "people"]]
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    s = scores[["score"]].sort_values(by = "score", ascending = False)
    s["rank"] = (s != s.shift().fillna(-1)).cumsum()
    return s
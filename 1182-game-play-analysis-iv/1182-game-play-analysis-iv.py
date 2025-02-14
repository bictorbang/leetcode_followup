import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    players = activity["player_id"].nunique()
    activity = activity.sort_values(by= ["player_id", "event_date"]).groupby("player_id").head(2)
    activity["date_diff"] = activity.groupby("player_id")["event_date"].diff()
    num = len(activity[activity["date_diff"] == pd.Timedelta(days = 1)][["player_id"]].drop_duplicates())
    return pd.DataFrame({"fraction" : [round(num / players, 2)]})

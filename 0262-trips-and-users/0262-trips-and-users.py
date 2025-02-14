import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame: 
    trips = trips[(trips["request_at"] >= "2013-10-01") & (trips["request_at"] <= "2013-10-03")]
    mask = users[users["banned"] == "Yes"]["users_id"]
    trips = trips[(~trips["client_id"].isin(mask)) & (~trips["driver_id"].isin(mask))]
    return trips.groupby("request_at")["status"].apply(lambda x : x.str.contains("cancelled").mean().round(2)).reset_index().rename(columns={"request_at":"Day","status":"Cancellation Rate"})
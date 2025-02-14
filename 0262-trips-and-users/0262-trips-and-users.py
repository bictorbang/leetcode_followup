import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips = trips[(trips["request_at"] >= "2013-10-01") & (trips["request_at"] <= "2013-10-03")]
    mask = users[users["banned"] == "Yes"]["users_id"]
    trips = trips[(~trips["client_id"].isin(mask)) & (~trips["driver_id"].isin(mask))]
    cancelled = trips[trips["status"] != "completed"][["request_at", "status"]].groupby("request_at").count().reset_index()
    total = trips[["request_at", "status"]].groupby("request_at").count().reset_index()
    end = total.merge(cancelled, on = "request_at", how = "left").rename(columns = {"request_at" : "Day"}).fillna(0)
    end["Cancellation Rate"] = round(end["status_y"] / end["status_x"], 2)
    return end[["Day", "Cancellation Rate"]]
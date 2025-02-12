import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates().sort_values("product")
    activities["products"] = activities.groupby("sell_date")[["product"]].transform(lambda x : ','.join(x))
    return activities[["sell_date", "products"]].drop_duplicates().merge(activities.groupby("sell_date")[["products"]].count().rename({"products" : "num_sold"}, axis = 1), on = "sell_date")[["sell_date", "num_sold", "products"]].sort_values("sell_date")
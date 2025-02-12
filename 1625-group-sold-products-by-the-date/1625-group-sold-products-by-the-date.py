import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates().sort_values("product")
    return activities.groupby("sell_date").agg(num_sold = ("sell_date", "size"), products = ("product", (lambda x : ",".join(x)))).reset_index().sort_values("sell_date")
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.drop("order_date", axis = 1).merge(sales_person[["sales_id", "name"]], how = "right").merge(company[["com_id", "name"]], on = "com_id", suffixes = (None, "_y"), how = "left")
    names = df[df["name_y"] == "RED"]["name"].values
    return df.drop(df[df["name"].isin(names)].index)[["name"]].drop_duplicates()
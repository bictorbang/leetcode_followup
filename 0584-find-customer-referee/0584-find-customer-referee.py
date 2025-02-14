import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer.loc[(customer["referee_id"].fillna(0) != 2), ["name"]]
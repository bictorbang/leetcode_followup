import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    products = len(product)
    cnt = customer.groupby("customer_id").nunique().reset_index()
    return cnt[cnt["product_key"] == products][["customer_id"]]
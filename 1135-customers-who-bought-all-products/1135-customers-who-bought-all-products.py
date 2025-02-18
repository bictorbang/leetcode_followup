import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    products = len(product)
    cnt = customer.drop_duplicates().groupby("customer_id").count().reset_index()
    return cnt[cnt["product_key"] == products][["customer_id"]]
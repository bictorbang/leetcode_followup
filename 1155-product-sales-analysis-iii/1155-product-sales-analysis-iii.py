import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    sales["rank"] = sales.groupby("product_id")["year"].rank(method = "dense")
    return sales.loc[sales["rank"] == 1].merge(product).iloc[:, [1, 2, 3, 4]].rename(columns = {"year": "first_year"})
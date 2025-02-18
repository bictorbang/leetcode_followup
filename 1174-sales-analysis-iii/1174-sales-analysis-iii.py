import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    rg = sales.groupby("product_id").agg(min_sale = ("sale_date", "min"), max_sale = ("sale_date", "max")).reset_index()
    return rg.loc[(rg.min_sale >= "2019-01-01") & (rg.max_sale <= "2019-03-31"), ["product_id"]].merge(product[["product_id", "product_name"]])
